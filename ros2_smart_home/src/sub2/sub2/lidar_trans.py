import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point32, TransformStamped
from sensor_msgs.msg import LaserScan, PointCloud
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu
from squaternion import Quaternion
from math import pi, cos, sin
import tf2_ros

class lidarTrans(Node):
    def __init__(self):
        super().__init__('lidar_trans')
        self.lidar_sub = self.create_subscription(LaserScan, '/scan', self.lidar_callback, 10)
        self.pcd_pub = self.create_publisher(PointCloud, 'pcd', 10)
        self.odom_sub = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)
        self.imu_sub = self.create_subscription(Imu, '/imu', self.imu_callback, 10)
        self.odom_msg = Odometry()
        self.is_odom = False
        self.is_imu = False
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0

    def odom_callback(self, msg):
        self.is_odom = True
        self.odom_msg = msg
        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y
        # 로봇의 방향 각도를 오도메트리 메시지에서 직접 추출
        q = Quaternion(msg.pose.pose.orientation.w,
                       msg.pose.pose.orientation.x,
                       msg.pose.pose.orientation.y,
                       msg.pose.pose.orientation.z)
        roll, pitch, self.theta = q.to_euler()

    def imu_callback(self, msg):
        if not self.is_imu:
            self.is_imu = True
            imu_q = Quaternion(msg.orientation.w, msg.orientation.x, msg.orientation.y, msg.orientation.z)
            imu_roll, imu_pitch, imu_yaw = imu_q.to_euler()
            # imu로부터 받은 각도를 오도메트리의 방향에 더함
            self.theta += imu_yaw
        else:
            imu_q = Quaternion(msg.orientation.w, msg.orientation.x, msg.orientation.y, msg.orientation.z)
            imu_roll, imu_pitch, imu_yaw = imu_q.to_euler()
            self.theta = imu_yaw

    def lidar_callback(self, msg):
        if self.is_odom and self.is_imu:
            pcd_msg = PointCloud()
            pcd_msg.header.frame_id = 'map'

            for angle, r in enumerate(msg.ranges):
                lidar_point = Point32()

                if 0.0 < r < 12:
                    lidar_point.x = self.x + r * cos((angle - 90) * pi / 180)
                    lidar_point.y = self.y + r * sin((angle - 90) * pi / 180)
                    pcd_msg.points.append(lidar_point)

            self.pcd_pub.publish(pcd_msg)

def main(args=None):
    rclpy.init(args=args)
    lidar_trans = lidarTrans()
    rclpy.spin(lidar_trans)
    lidar_trans.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
