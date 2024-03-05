import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point32
from sensor_msgs.msg import LaserScan, PointCloud
from nav_msgs.msg import Odometry
from math import pi, cos, sin
import tf2_ros

class lidarTrans(Node):
    def __init__(self):
        super().__init__('lidar_trans')
        self.lidar_sub = self.create_subscription(LaserScan, '/scan', self.lidar_callback, 10)
        self.pcd_pub = self.create_publisher(PointCloud, 'pcd', 10)
        self.subscription = self.create_subscription(Odometry,'/odom',self.listener_callback,10)
        self.odom_msg=Odometry()
        self.is_odom=False
    
    def listener_callback(self,msg):
        self.is_odom=True
        self.odom_msg=msg

    def lidar_callback(self, msg):
        pcd_msg=PointCloud()
        pcd_msg.header.frame_id='map'
        x=self.odom_msg.pose.pose.position.x
        y=self.odom_msg.pose.pose.position.y
        for angle, r in enumerate(msg.ranges):
            lidar_point=Point32()

            if 0.0<r<12:
                lidar_point.x=x+r*cos(angle*pi/180)
                lidar_point.y=y+r*sin(angle*pi/180)
                pcd_msg.points.append(lidar_point)

        self.pcd_pub.publish(pcd_msg)

def main(args=None):
    rclpy.init(args=args)
    lidar_trans = lidarTrans()
    rclpy.spin(lidar_trans)
    lidar_trans.destroy_node()
    rclpy.shutdown()



if __name__=='__main__':
    main()