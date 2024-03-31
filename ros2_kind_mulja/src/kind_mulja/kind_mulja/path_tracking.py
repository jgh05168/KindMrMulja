import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist,Point32
from ssafy_msgs.msg import TurtlebotStatus, Col
from squaternion import Quaternion
from nav_msgs.msg import Odometry,Path
from math import pi,cos,sin,sqrt,atan2
import numpy as np
import time
from sensor_msgs.msg import LaserScan, PointCloud

# path_tracking 노드는 로봇의 위치(/odom), 로봇의 속도(/turtlebot_status), 주행 경로(/local_path)를 받아서, 주어진 경로를 따라가게 하는 제어 입력값(/cmd_vel)을 계산합니다.
# 제어입력값은 선속도와 각속도로 두가지를 구합니다. 


# 노드 로직 순서
# 1. 제어 주기 및 타이머 설정
# 2. 파라미터 설정
# 3. Quaternion 을 euler angle 로 변환
# 4. 터틀봇이 주어진 경로점과 떨어진 거리(lateral_error)와 터틀봇의 선속도를 이용해 전방주시거리 계산
# 5. 전방 주시 포인트 설정
# 6. 전방 주시 포인트와 로봇 헤딩과의 각도 계산
# 7. 선속도, 각속도 정하기


class followTheCarrot(Node):

    def __init__(self):
        super().__init__('path_tracking')
        self.cmd_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.subscription = self.create_subscription(Odometry,'/odom',self.odom_callback,10)
        self.status_sub = self.create_subscription(TurtlebotStatus,'/turtlebot_status',self.status_callback,10)
        self.path_sub = self.create_subscription(Path,'/local_path',self.path_callback,10)
        self.lidar_sub = self.create_subscription(LaserScan,"/scan",self.lidar_callback,10) 
        self.path_pcd_pub = self.create_publisher(PointCloud, 'path_pcd', 10)
        self.col_pub = self.create_publisher(Col, '/col', 10)
        # 로직 1. 제어 주기 및 타이머 설정
        time_period=0.05 
        self.timer = self.create_timer(time_period, self.timer_callback)

        self.is_odom=False
        self.is_path=False
        self.is_status=False

        self.is_lidar = False       # 라이다 메시지 수신여부 및 쟁애물 충돌 여부 저장 변수
        self.collision = False
        self.lidar_msg=LaserScan()

        self.odom_msg=Odometry()            
        self.robot_yaw=0.0
        self.path_msg=Path()
        self.cmd_msg=Twist()
        
        # 로직 2. 파라미터 설정
        self.lfd=0.1
        self.min_lfd=0.1
        self.max_lfd=2.0
        

    def timer_callback(self):

        if self.is_status and self.is_odom and self.is_path:

            if len(self.path_msg.poses) > 2:
                self.is_look_forward_point= False
                
                # 로봇의 현재 위치를 나타내는 변수
                robot_pose_x=self.odom_msg.pose.pose.position.x
                robot_pose_y=self.odom_msg.pose.pose.position.y

                lateral_error= sqrt(pow(self.path_msg.poses[0].pose.position.x-robot_pose_x,2)+pow(self.path_msg.poses[0].pose.position.y-robot_pose_y,2))
                # print(robot_pose_x,robot_pose_y,lateral_error)
                
                # 로직 4. 로봇이 주어진 경로점과 떨어진 거리(lateral_error)와 로봇의 선속도를 이용해 전방주시거리 설정
                self.lfd=(self.status_msg.twist.linear.x + lateral_error) * 0.71

                if self.lfd < self.min_lfd :
                    self.lfd=self.min_lfd
                if self.lfd > self.max_lfd:
                    self.lfd=self.max_lfd

                min_dis=float('inf')
                
                # 로직 5. 전방 주시 포인트 설정
                for num ,waypoint in enumerate(self.path_msg.poses) :

                    self.current_point=waypoint.pose.position
                    dis=sqrt(pow(self.path_msg.poses[0].pose.position.x - self.current_point.x, 2) + pow(self.path_msg.poses[0].pose.position.y - self.current_point.y, 2))
                    if abs(dis-self.lfd) < min_dis :
                        min_dis=abs(dis-self.lfd)
                        self.forward_point=self.current_point
                        self.is_look_forward_point=True


                    
                if self.is_look_forward_point and self.collision == False:

                    global_forward_point=[self.forward_point.x ,self.forward_point.y,1]

                    '''
                    로직 6. 전방 주시 포인트와 로봇 헤딩과의 각도 계산

                    (테스트) 맵에서 로봇의 위치(robot_pose_x,robot_pose_y)가 (5,5)이고, 헤딩(self.robot_yaw) 1.57 rad 일 때, 선택한 전방포인트(global_forward_point)가 (3,7)일 때
                    변환행렬을 구해서 전방포인트를 로봇 기준좌표계로 변환을 하면 local_forward_point가 구해지고, atan2를 이용해 선택한 점과의 각도를 구하면
                    theta는 0.7853 rad 이 나옵니다.
                    trans_matrix는 로봇좌표계에서 기준좌표계(Map)로 좌표변환을 하기위한 변환 행렬입니다.
                    det_tran_matrix는 trans_matrix의 역행렬로, 기준좌표계(Map)에서 로봇좌표계로 좌표변환을 하기위한 변환 행렬입니다.  
                    local_forward_point 는 global_forward_point를 로봇좌표계로 옮겨온 결과를 저장하는 변수입니다.
                    theta는 로봇과 전방 주시 포인트와의 각도입니다. 
                    '''
                    trans_matrix =np.array([
                        [cos(self.robot_yaw), -sin(self.robot_yaw), robot_pose_x],
                        [sin(self.robot_yaw), cos(self.robot_yaw), robot_pose_y],
                        [0,0,1]
                    ])
                    det_trans_matrix=np.linalg.inv(trans_matrix)
                    local_forward_point = det_trans_matrix.dot(global_forward_point)
                    theta = -atan2(local_forward_point[1], local_forward_point[0]) 
                    
                    # 로직 7. 선속도, 각속도 정하기
                    out_vel=0.7
                    out_rad_vel=theta*1.55

                    self.cmd_msg.linear.x=out_vel
                    self.cmd_msg.angular.z=out_rad_vel


           
            else :
                # print("no found forward point")
                self.cmd_msg.linear.x=0.0
                self.cmd_msg.angular.z=0.0

            
            self.cmd_pub.publish(self.cmd_msg)

    def lidar_callback(self, msg):
        
        self.is_lidar = True
        self.lidar_msg = msg
        # 충돌체크를 하기 위해서는 경로와 위치 데이터를 알고 있어야 함
        if self.is_odom == True:
            col_msg=Col()
            # pcd 메세지를 전달하기 위한 설정
            # 포인트글라우드 타입의 데이터 선언 : 직교좌표계 사용을 위해서
            pcd_msg=PointCloud()
            pcd_msg.header.frame_id = 'map'

            # Local의 데이터를 Global로 변환 할 것이므로 변환행렬 만들어서 진행
            pose_x=self.odom_msg.pose.pose.position.x
            pose_y=self.odom_msg.pose.pose.position.y
            theta = self.robot_yaw
            t = np.array([
                [cos(theta),-sin(theta),pose_x],
                [sin(theta),cos(theta),pose_y],
                [0,0,1]
            ])
            
            # 극좌표계를 직교좌표계로 변환

            for angle, r in enumerate(msg.ranges[:-1]):
                global_point=Point32()      # 로봇(global) 극좌표 정보

                if 0.0 < r < 12:
                    # 극좌표계를 직교 좌표계로 바꿔주고
                    local_x = r*cos(( angle + 180 ) * pi / 180)
                    local_y = r*sin(( angle + 180 ) * pi / 180)
                    local_point = np.array([[local_x],[local_y],[1]])
                    # 해당 좌표는 로봇 기준의 LOCAL 좌표이므로 GLOBAL 좌표로 바꿔줌
                    global_result=t.dot(local_point)
                    global_point.x = global_result[0][0]
                    global_point.y = global_result[1][0]
                    # 바꾼 점들을 넣어줌
                    pcd_msg.points.append(global_point)
           
            # pcd_msg 를 publish해서 확인
            self.path_pcd_pub.publish(pcd_msg)

            self.collision = False

            # 모든 경로점과 모든 라이더간의 거리를 비교
            for waypoint in self.path_msg.poses:
                for lidar_point in pcd_msg.points:
                    distance = sqrt(pow(waypoint.pose.position.x-lidar_point.x,2)+pow(waypoint.pose.position.y-lidar_point.y,2))
                    if distance < 0.06: # 0.1 m 보다 작으면 충돌이 일어난다고 가정
                        ### 아마 여기에 주로 코드를 작성하게 될 듯 ###
                        self.collision = True

            col_msg.col = self.collision
            self.col_pub.publish(col_msg)


    def odom_callback(self, msg):
        self.is_odom=True
        self.odom_msg=msg
        
        # 로직 3. Quaternion 을 euler angle 로 변환
        q=Quaternion(msg.pose.pose.orientation.w,msg.pose.pose.orientation.x,msg.pose.pose.orientation.y,msg.pose.pose.orientation.z)
        _,_,self.robot_yaw = q.to_euler()

    
    def path_callback(self, msg):
        self.is_path=True
        self.path_msg=msg


    def status_callback(self,msg):
        self.is_status=True
        self.status_msg=msg
        
        
def main(args=None):
    rclpy.init(args=args)
    path_tracker = followTheCarrot()
    rclpy.spin(path_tracker)
    path_tracker.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()