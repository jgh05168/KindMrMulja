import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import OccupancyGrid, MapMetaData
from geometry_msgs.msg import Pose, Point, TransformStamped
from squaternion import Quaternion
from math import cos, sin, pi
import numpy as np
import tf2_ros

class LocalGridMap(Node):
    def __init__(self):
        super().__init__('local_grid_map')
        self.create_subscription(LaserScan, '/scan', self.lidar_callback, 10)
        self.create_subscription(Pose, '/robot_pose', self.robot_pose_callback, 10)  # 수정된 부분
        self.map_pub = self.create_publisher(OccupancyGrid, '/local_map', 10)

        # Initialize map parameters
        self.resolution = 0.05  # Map resolution in meters per pixel
        self.map_size = (100, 100)  # Map size in pixels (width, height)
        self.map_center = (-50, -50)  # Initial map center coordinates in pixels

        # Initialize the local grid map
        self.local_map = np.zeros(self.map_size, dtype=np.int8)

        # Initialize map metadata
        self.map_metadata = MapMetaData()
        self.map_metadata.resolution = self.resolution
        self.map_metadata.width = self.map_size[0]
        self.map_metadata.height = self.map_size[1]
        self.map_metadata.origin = Pose(position=Point(x=-50.0, y=-50.0))

        # Initialize tf2 broadcaster
        self.tf_broadcaster = tf2_ros.TransformBroadcaster(self)

        # Variables to store robot pose
        self.x = 0
        self.y = 0
        self.theta = 0

    def robot_pose_callback(self, msg):  # 수정된 부분
        # Update robot pose based on pose data
        self.x = msg.position.x
        self.y = msg.position.y
        q = Quaternion(msg.orientation.w, msg.orientation.x, msg.orientation.y, msg.orientation.z)
        _, _, self.theta = q.to_euler()

        # Update map center to robot's current position
        self.map_center = (int(-50 + self.x / self.resolution),
                           int(-50 + self.y / self.resolution))

        # Broadcast tf2 transform from "map" to "base_link"
        self.broadcast_tf2_transform()

        # Update the local grid map
        self.update_local_map()
        self.publish_local_map()

    def lidar_callback(self, msg):
        # Process lidar data and update the local grid map
        angles = np.arange(msg.angle_min, msg.angle_max, msg.angle_increment)
        ranges = np.array(msg.ranges)
        self.update_local_map(angles, ranges)
        self.publish_local_map()

    def update_local_map(self, angles=None, ranges=None):
        # Clear the local grid map
        self.local_map = np.zeros(self.map_size, dtype=np.int8)

        # Process lidar data and update the local grid map
        if angles is not None and ranges is not None:
            for angle, dist in zip(angles, ranges):
                # Calculate the endpoint of the laser ray in the map coordinates
                end_x = self.x + dist * cos(angle + self.theta)
                end_y = self.y + dist * sin(angle + self.theta)

                # Convert the endpoint to pixel coordinates in the local map
                map_x = int((end_x / self.resolution) + self.map_center[0])
                map_y = int((end_y / self.resolution) + self.map_center[1])

                # Update the corresponding cell in the local map
                if 0 <= map_x < self.map_size[0] and 0 <= map_y < self.map_size[1]:
                    self.local_map[map_y, map_x] = 100  # Occupied cell

    def publish_local_map(self):
        # Create and publish OccupancyGrid message
        map_msg = OccupancyGrid()
        map_msg.header.frame_id = 'map'
        map_msg.info = self.map_metadata
        map_msg.data = np.ravel(self.local_map).tolist()
        self.map_pub.publish(map_msg)

    def broadcast_tf2_transform(self):
        # Broadcast transform from "map" to "base_link"
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = "map"
        t.child_frame_id = "base_link"
        t.transform.translation.x = self.x
        t.transform.translation.y = self.y
        t.transform.translation.z = 0.0
        q = Quaternion.from_euler(0, 0, self.theta)
        t.transform.rotation.x = q.x
        t.transform.rotation.y = q.y
        t.transform.rotation.z = q.z
        t.transform.rotation.w = q.w
        self.tf_broadcaster.sendTransform(t)

def main(args=None):
    rclpy.init(args=args)
    local_grid_map = LocalGridMap()
    rclpy.spin(local_grid_map)
    local_grid_map.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
