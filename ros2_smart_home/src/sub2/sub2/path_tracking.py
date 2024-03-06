import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist,Point, Point32
from ssafy_msgs.msg import TurtlebotStatus
from squaternion import Quaternion
from nav_msgs.msg import Odometry, Path
# ^ 필요한 메시지 타입들 
from math import pi, cos, sin, sqrt, atan2
import numpy as np # 행렬 연산을 위해
# 라이다 메시지타입 import 
from sensor_msgs.msg import LaserScan, PointCloud


class followTheCarrot(Node):

    def __init__(self):
        super().__init__('path_tracking')
        # 로봇의 위치(/odom), 로봇의 상태(/turtlebot_status), 경로(/local_path)를 받아
        # 로봇의 제어 입력(/cmd_vel) 을 보내주기 위한 publish, subscriber 생성
        self.cmd_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.odom_sub = self.create_subscription(Odometry, '/odom', self.odom_callback,10)
        # 터틀봇의 현재 속도를 받아와서 전방주시거리를 설정할 거임
        self.status_sub  = self.create_subscription(TurtlebotStatus, '/turtlebot_status', self.status_callback,10)
        self.path_sub = self.create_subscription(Path, '/local_path', self.path_callback,10)
        # 라이다 데이터를 받기 위해  데이터 타입, 라이다 토픽을 이용해 subscriber 생성
        self.lidar_sub = self.create_subscription(LaserScan,"/scan",self.lidar_callback,10) 
        self.pcd_pub =self.create_publisher(PointCloud, 'pcd',10)

        time_period = 0.05
        self.timer = self.create_timer(time_period, self.timer_callback)

        self.is_odom = False
        self.is_path = False
        self.is_status = False
        # 라이다 메시지 수신여부 및 쟁애물 충돌 여부 저장 변수
        self.is_lidar = False
        self.collision = False

        self.odom_msg= Odometry()
        self.path_msg=Path()
        self.cmd_msg=Twist()
        self.lidar_msg=LaserScan() # 라이다 메시지를 저장한 변수 생성
        self.robot_yaw = 0.0

        #  단위 m
        self.lfd = 0.1 # 초기값 : L 값 = 전방주시 거리 
        self.min_lfd = 0.1 # 최소 전방주시거리
        self.max_lfd = 2.0 # 최대 전방주시거리

    def timer_callback(self):

        # 계산에 필요한 데이터 다 들어왔는지 확인 + lidar 데이터 확인도 추가
        if self.is_status and self.is_odom == True and self.is_path == True and self.is_lidar==True:
            if len(self.path_msg.poses) > 1:
                self.is_look_forward_point = False

                # odom 으로 받은 x,y 좌표 저장
                robot_pose_x = self.odom_msg.pose.pose.position.x
                robot_pose_y = self.odom_msg.pose.pose.position.y
                # 로봇이 목표경로로부터 떨어진 거리 계산
                lateral_error = sqrt(pow(self.path_msg.poses[0].pose.position.x - robot_pose_x,2)+pow(self.path_msg.poses[0].pose.position.y-robot_pose_y,2))

                # 로봇의 선속도, 경로로 부터 떨어진 거리를 이용해 전방주시거리 결정
                self.lfd=(self.status_msg.twist.linear.x + lateral_error) * 1
                # 전방 주시거리가 최소 최대 넘어가면 제한하기
                if self.lfd < self.min_lfd:
                    self.lfd = self.min_lfd
                if self.lfd > self.max_lfd:
                    self.lfd = self.max_lfd
                print(self.lfd)

                min_dis=float('inf')

                for num, waypoint in enumerate(self.path_msg.poses):
                    self.current_point = waypoint.pose.position
                    
                    # 로봇과 가장 가까운 경로점과 모든 경로점과의 거리 탐색
                    dis = sqrt(pow(self.path_msg.poses[0].pose.position.x - self.current_point.x,2) + pow(self.path_msg.poses[0].pose.position.y - self.current_point.y,2))
                    # 전방 주시거리에 가장 가깝게 있는 경로점 선택
                    if abs(dis-self.lfd) < min_dis:
                        min_dis = abs(dis-self.lfd)
                        self.forward_point = self.current_point
                        self.is_look_forward_point=True


                if self.is_look_forward_point :
                    # 전방주시포인트를 로봇좌표계로 변경후, 로봇과 전방주시포인트와의 각도 게산
                    global_forward_point = [self.forward_point.x,self.forward_point.y,1]

                    # 로봇의 현재 위치(x,y),회전(yaw)값을 이용해 변환 행렬을 만든다
                    trans_matrix =np.array([
                        [cos(self.robot_yaw), -sin(self.robot_yaw),robot_pose_x],
                        [sin(self.robot_yaw), cos(self.robot_yaw),robot_pose_y],
                        [0,0,1]
                    ])

                    # 변환 행렬의 역행렬을 구한다
                    det_trans_matrix=np.linalg.inv(trans_matrix)
                    # 변환 행렬의 역행렬과 경로점을 행렬곱 연산을 해서 로봇좌계에서 표현되는 경로점을 구한다.
                    # GLOBAL 경로가 로봇기준의 LOCAL 경로로 바뀌게 됨
                    local_forward_point = det_trans_matrix.dot(global_forward_point)
                    # 우리가 제어할 각속도 값 = 로봇과 내가 찾은 전방주시 포인트 간의 차이값
                    theta = -atan2(local_forward_point[1], local_forward_point[0])

                    out_vel=2.0
                    out_rad_vel=theta*4.0

                    self.cmd_msg.linear.x=out_vel
                    self.cmd_msg.angular.z=out_rad_vel

                    # 충돌체크 후 충돌이 일어난다면 정지
                    if self.collision == True:
                        self.cmd_msg.linear.x = 0.0

            else:
                # 찾은 전방주시 거리가 만족되지 않는 포인트라면
                print("no found forward point")
                # 터틀봇을 움직이지 않게 설정
                self.cmd_msg.linear.x = 0.0
                self.cmd_msg.angular.z = 0.0
            
            # 터틀봇 제어 퍼블리셔로 제어 메세지 전송
            self.cmd_pub.publish(self.cmd_msg)


    # 라이다 데이터가 들어오는 콜백 함수
    def lidar_callback(self, msg):
        self.lidar_msg = msg
        # 충돌체크를 하기 위해서는 경로와 위치 데이터를 알고 있어야 함
        if self.is_path == True and self.is_odom == True:

            # 포인트글라우드 타입의 데이터 선언 : 직교좌표계 사용
            pcd_msg=PointCloud()
            pcd_msg.header.frame_id = 'map'

            # 로컬의 데이터를 글로벌로 변환 할 것이므로 변환행렬 만들어서 진행
            pose_x=self.odom_msg.pose.pose.position.x
            pose_y=self.odom_msg.pose.pose.position.y
            theta = self.robot_yaw
            t = np.array([
                [cos(theta),-sin(theta),pose_x],
                [sin(theta),cos(theta),pose_y],
                [0,0,1]
            ])
            
            # 극좌표계를 직교좌표계로 변환
            for angle, r in enumerate(msg.ranges):
                global_point=Point32()

                if 0.0 < r < 12:
                    # 극좌표계를 직교 좌표계로 바꿔주고
                    local_x = r*cos(angle*pi/180)
                    local_y = r*sin(angle*pi/180)
                    local_point = np.array([[local_x],[local_y],[1]])
                    # 해당 좌표는 로봇 기준의 LOCAL 좌표이므로 GLOBAL 좌표로 바꿔줌
                    global_result=t.dot(local_point)
                    global_point.x = global_result[0][0]
                    global_point.y = global_result[1][0]
                    # 바꾼 점들을 넣어줌
                    pcd_msg.points.append(global_point)
                    # 만약에 이 데이터를 글로벌에서 찍히는 지 보고 싶으면
                    # pcd_msg 를 publish해서 확인할 수 있음
                    self.pcd_pub.publish(pcd_msg)

            self.collision = False
            # 모든 경로점과 모든 라이더간의 거리를 비교
            for waypoint in self.path_msg.poses:
                for lidar_point in pcd_msg.points:
                    distance = sqrt(pow(waypoint.pose.position.x-lidar_point.x,2)+pow(waypoint.pose.position.y-lidar_point.y,2))
                    if distance < 0.1 : # 0.1 m 보다 작으면 충돌이 일어난다고 가정
                        self.collision = True # 충돌이라고 체크
                        print('collision')
            self.is_lidar = True

    # odom 토픽을 받아 위치저장, 쿼터니언을 오일러각으로 변환해서 로봇의 yaw 로 사용
    def odom_callback(self,msg):
        self.is_odom = True
        self.odom_msg=msg
        q=Quaternion(msg.pose.pose.orientation.w,msg.pose.pose.orientation.x,msg.pose.pose.orientation.y,msg.pose.pose.orientation.z)
        _,_,self.robot_yaw = q.to_euler()

    # 경로 데이터 저장
    def path_callback(self,msg):
        self.is_path = True
        self.path_msg = msg

    # 상태 데이터 저장
    def status_callback(self, msg):
        self.is_status = True
        self.status_msg=msg


def main(args=None):
    rclpy.init(args=args)
    path_tracking = followTheCarrot()
    rclpy.spin(path_tracking)
    path_tracking.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()    
