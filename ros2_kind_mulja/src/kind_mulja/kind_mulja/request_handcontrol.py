import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped
from ssafy_msgs.msg import RequestHandControl,TurtlebotStatus,TargetGrid,WorkStatus
import time
# 위치에 따른 물건 들고 내리기 로직 
# 1. 로봇 위치를 받아온다. 
# 2. 물건 위치를 받아온다. 
# 3. 물건 위치에서 물건을 인식하고 들어올린다. 
# 4. 물건을 들고 이동한다. 
# 5. 목적지 위치를 받아온다. 
# 6. 목적이 위치에서 물건 둘곳을 확인하고 내려놓는다. 

class RequestMsgHandControl(Node):
    def __init__(self):
        super().__init__('request_handcontrol')
        
        
        # 1. 로봇 위치
        self.odom_subscriber = self.create_subscription(Odometry,'/odom',self.listener_callback,10)
        self.turtlebot_status = self.create_subscription(TurtlebotStatus,'/turtlebot_status',self.turtlebot_status_cb,10)

        # 2. 상품 및 트럭 위치 subscription
        self.target_grid_sub=self.create_subscription(TargetGrid,'/target_grid',self.target_grid_cb,10)

        
        # 3. 충전소 위치
        # self.goal_sub = self.create_subscription(PoseStamped,'goal_pose', self.goal_callback, 1)
    
        
        # request 요청 publisher 생성
        self.request_handcontrol_publisher=self.create_publisher(RequestHandControl,'/request_handcontrol',10)
        self.target_publisher=self.create_publisher(PoseStamped,'goal_pose',10)
        self.work_status_publisher=self.create_publisher(WorkStatus,'/work_status',10)
        
        ## 제어 메시지 변수 생성 
        #subscriber
        self.is_odom=False
        self.odom_msg=Odometry()
        self.is_turtlebot_status=False
        self.turtlebot_status_msg=TurtlebotStatus()
        self.goal_msg=PoseStamped()
        self.target_grid_msg=TargetGrid()
        
        
        #publisher
        self.request_hand_control_msg=RequestHandControl()
        self.request_target_msg=PoseStamped()
        self.work_status_msg=WorkStatus()
        
        self.product_is_done=False
        self.truct_is_done=False
        self.charge_is_done=False
        
        # Timer 1초마다 실행 
        self.timer = None
        
        
    def listener_callback(self,msg):
        self.is_odom=True
        self.odom_msg=msg
        
    def goal_callback(self,msg):
        if msg.header.frame_id == 'map':
            self.goal_x, self.goal_y = msg.pose.position.x, msg.pose.position.y
        
    def turtlebot_status_cb(self,msg):
        self.is_turtlebot_status=True
        self.turtlebot_status_msg=msg
        
    def target_grid_cb(self,msg):
        self.target_grid_msg=msg
        # print("callback fun: ", self.target_grid_msg)
        self.moving_x=self.target_grid_msg.moving_zone_x
        self.moving_y=self.target_grid_msg.moving_zone_y
        self.product_x=self.target_grid_msg.product_x
        self.product_y=self.target_grid_msg.product_y
        self.charge_x=self.target_grid_msg.charge_x
        self.charge_y=self.target_grid_msg.charge_y
        self.order_detail_id=self.target_grid_msg.order_detail_id
        # print("msg: ",msg)
        
        self.product_is_done=False
        self.truct_is_done=False
        
        self.timer = self.create_timer(5, self.timer_callback)
        # self.move_to_goal()
        
        
    def timer_callback(self):  
    # def move_to_goal(self):
        turtle_x=self.odom_msg.pose.pose.position.x
        turtle_y=self.odom_msg.pose.pose.position.y
        

        # 4. 백엔드로 부터 좌표를 받으면 target_grid_msg 기반으로 물건 앞으로 이동하라고 publish한다.  
        if self.target_grid_msg and self.product_is_done==False:
        # if self.product_initialized and not self.product_is_done:
            # print(self.target_grid_msg.product_x)
            # print(self.target_grid_msg.product_y)
            self.request_target_msg.header.frame_id = 'map'
            self.request_target_msg.pose.position.x=self.product_x
            self.request_target_msg.pose.position.y=self.product_y
            self.target_publisher.publish(self.request_target_msg)
            print(self.request_target_msg)

            self.work_status_msg.is_start=True
            self.work_status_msg.order_detail_id=self.order_detail_id
            self.work_status_publisher.publish(self.work_status_msg)
            
            self.product_is_done=True
        else: 
            print("request_target is None")

        
        # 5. 물건을 든다. 
        # 터틀봇의 위치가 사물의 위치랑 가까워 졌을 때 
        if abs(turtle_x-self.product_x) <=1 and abs(turtle_y-self.product_y)<=1:
            
            # 터틀봇 상태가 ture이고 can_lift가 ture인경우
            if self.is_turtlebot_status and self.turtlebot_status_msg.can_lift:
                self.request_hand_control_msg.control_mode=2        
                self.request_handcontrol_publisher.publish(self.request_hand_control_msg)     
    
            if self.turtlebot_status_msg.can_use_hand:
                # 6. 물건을 들고 트럭으로 이동한다. 
                self.request_target_msg.header.frame_id = 'map'
                    # self.moving_x=self.target_grid_msg.moving_zone_x
                    # self.moving_y=self.target_grid_msg.moving_zone_y
                self.request_target_msg.pose.position.x=self.moving_x
                self.request_target_msg.pose.position.y=self.moving_y
                self.target_publisher.publish(self.request_target_msg)
                # print(self.request_target_msg)
                

            
    
        # 7. 로봇은 목적지에 위치한다. 
    #     x=self.odom_msg.pose.pose.position.x
    #     y=self.odom_msg.pose.pose.position.y
    #   터틀봇의 위치가 트럭의 위치랑 가까워졌을 때
            
        if self.truct_is_done==False and abs(turtle_x-self.moving_x)<=1 and abs(turtle_y-self.moving_y)<=1:
    #     if abs(self.moving_x-x)<=1 and abs(self.moving_y-y)<=1:
            
            # 8. 물건 preview
            if self.turtlebot_status_msg.can_use_hand:
                self.request_hand_control_msg.control_mode=1        
                self.request_handcontrol_publisher.publish(self.request_hand_control_msg) 
            
            
    #         # 9. 물건을 내려놓는다.
            if self.turtlebot_status_msg.can_put:
                self.request_hand_control_msg.control_mode=3        
                self.request_handcontrol_publisher.publish(self.request_hand_control_msg) 

                
                self.work_status_msg.is_start=False
                self.work_status_msg.order_detail_id=self.order_detail_id
                self.work_status_publisher.publish(self.work_status_msg)
                
                time.sleep(5)
                
                self.truct_is_done=True
 
            
    #         # 목적지 주소를 전달한다.
        if self.turtlebot_status_msg.can_use_hand==False and self.work_status_msg.is_start==False:
                
            self.request_target_msg.header.frame_id = 'map' 
            self.request_target_msg.pose.position.x=self.charge_x
            self.request_target_msg.pose.position.y=self.charge_y
            self.target_publisher.publish(self.request_target_msg) 
                
        

def main(args=None):
    rclpy.init(args=args)
    sub2_request_hand_control = RequestMsgHandControl()    
    rclpy.spin(sub2_request_hand_control)
    sub2_request_hand_control.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    
    
    
        


