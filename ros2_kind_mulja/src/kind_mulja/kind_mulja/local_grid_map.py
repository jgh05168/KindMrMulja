import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from squaternion import Quaternion
import numpy as np
from std_msgs.msg import Header
from nav_msgs.msg import OccupancyGrid  # 변경된 부분: OccupancyGrid 메시지를 추가

class LocalGridMap(Node):
    def __init__(self):
        super().__init__('local_grid_map')
        self.lidar_sub = self.create_subscription(LaserScan, '/scan', self.lidar_callback, 10)
        self.odom_sub = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)
        self.odom_msg = Odometry()
        self.is_odom = False
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
        self.map_resolution = 0.1
        self.map_size_x = 60
        self.map_size_y = 60
        self.map_center_x = -50.0
        self.map_center_y = -50.0
        self.local_grid_map = np.zeros((self.map_size_x, self.map_size_y), dtype=int)
        self.local_map_pub = self.create_publisher(OccupancyGrid, 'local_grid_map', 1)  # 변경된 부분: OccupancyGrid를 게시하기 위한 퍼블리셔 생성

    def odom_callback(self, msg):
        self.is_odom = True
        self.odom_msg = msg
        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y
        q = Quaternion(msg.pose.pose.orientation.w,
                       msg.pose.pose.orientation.x,
                       msg.pose.pose.orientation.y,
                       msg.pose.pose.orientation.z)
        roll, pitch, self.theta = q.to_euler()
        # 변경된 부분: 로봇의 위치가 변할 때 맵 중앙을 업데이트
        self.map_center_x = self.x - (self.map_size_x / 2) * self.map_resolution
        self.map_center_y = self.y - (self.map_size_y / 2) * self.map_resolution
        # 로봇의 위치가 변할 때마다 로컬 그리드를 0으로 초기화
        self.local_grid_map = np.zeros((self.map_size_x, self.map_size_y), dtype=int)

    def lidar_callback(self, msg):
        if self.is_odom:
            angle_min = msg.angle_min
            angle_increment = msg.angle_increment
            ranges = msg.ranges
            for i, range_data in enumerate(ranges):
                if range_data < msg.range_max and range_data > msg.range_min:
                    angle = self.theta + angle_min + i * angle_increment
                    x = self.x + range_data * np.cos(angle)
                    y = self.y + range_data * np.sin(angle)
                    map_x = int((x - self.map_center_x) / self.map_resolution)
                    map_y = int((y - self.map_center_y) / self.map_resolution)
                    if 0 <= map_x < self.map_size_x and 0 <= map_y < self.map_size_y:
                        # 로봇 위치에 해당하는 그리드 셀은 장애물로 표시하지 않음
                        if abs(map_x - int(self.map_size_x / 2)) < 2 and abs(map_y - int(self.map_size_y / 2)) < 2:
                            continue
                        self.local_grid_map[map_y, map_x] = 100 if range_data < 4.0 else 0
                        # 주변 좌표도 장애물로 표시
                        for dx in range(-3, 4):
                            for dy in range(-3, 4):
                                nx, ny = map_x + dx, map_y + dy
                                if 0 <= nx < self.map_size_x and 0 <= ny < self.map_size_y:
                                    self.local_grid_map[ny, nx] = 100
            # 변경된 부분: 로컬 그리드 맵을 좌우로 뒤집고 상하로 뒤집기
            flipped_map = np.flipud(np.fliplr(self.local_grid_map))
            # 변경된 부분: 로컬 그리드 맵을 OccupancyGrid 메시지로 변환하여 게시
            map_msg = OccupancyGrid()
            map_msg.header.stamp = self.get_clock().now().to_msg()
            map_msg.header.frame_id = 'map'
            map_msg.info.width = self.map_size_x
            map_msg.info.height = self.map_size_y
            map_msg.info.resolution = self.map_resolution
            map_msg.info.origin.position.x = self.map_center_x
            map_msg.info.origin.position.y = self.map_center_y
            map_msg.info.origin.position.z = 0.0
            map_msg.info.origin.orientation.x = 0.0
            map_msg.info.origin.orientation.y = 0.0
            map_msg.info.origin.orientation.z = 0.0
            map_msg.info.origin.orientation.w = 1.0
            map_data = flipped_map.flatten().tolist()
            map_msg.data = map_data
            self.local_map_pub.publish(map_msg)

def main(args=None):
    rclpy.init(args=args)
    local_grid_map = LocalGridMap()
    rclpy.spin(local_grid_map)
    local_grid_map.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
