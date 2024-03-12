import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped
from ssafy_msgs.msg import RequestHandControl,TurtlebotStatus,TargetGrid

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

        # 2. 트럭 위치
        self.truck_x=-16.0
        self.truck_y=-8.0
        
        # 3. 충전소 위치
        # self.goal_sub = self.create_subscription(PoseStamped,'goal_pose', self.goal_callback, 1)
        self.charge_x=-8.0
        self.charge_y=-4.0
        
        # 충전소 위치 임의 저장
        # self.target_publisher=self.create_publisher(TargetGrid,'/target_grid',1)
        self.target_publisher=self.create_publisher(PoseStamped,'/target_grid',1)
        # self.charge_site_x=10
        # self.charge_site_y=10
        
        # request 요청 publisher 생성
        self.request_handcontrol_publisher=self.create_publisher(RequestHandControl,'/request_handcontrol',10)
        
        ## 제어 메시지 변수 생성 
        #subscriber
        self.is_odom=False
        self.odom_msg=Odometry()
        self.is_turtlebot_status=False
        self.turtlebot_status_msg=TurtlebotStatus()
        self.goal_msg=PoseStamped()
        
        self.goal_x, self.goal_y=0,0
        
        #publisher
        self.request_hand_control_msg=RequestHandControl()
        self.request_target_msg=PoseStamped()
        
        # Timer 1초마다 실행 
        self.timer = self.create_timer(1, self.timer_callback)
        
    def listener_callback(self,msg):
        self.is_odom=True
        self.odom_msg=msg
        
    def goal_callback(self,msg):
        if msg.header.frame_id == 'map':
            self.goal_x, self.goal_y = msg.pose.position.x, msg.pose.position.y
        
    def turtlebot_status_cb(self,msg):
        self.is_turtlebot_status=True
        self.turtlebot_status_msg=msg
        
    def timer_callback(self):  
        
        # 4. 로봇은 물건 앞에 위치한다. 

        # self.target_publisher.publish(self.request_target_msg)
        
        # 5. 물건을 든다. 
        # 터틀봇 상태가 ture이고 can_lift가 ture인경우
        if self.is_turtlebot_status and self.turtlebot_status_msg.can_lift:
            self.request_hand_control_msg.control_mode=2        
            self.request_handcontrol_publisher.publish(self.request_hand_control_msg)     
 
            # 6. 물건을 들고 이동한다. 
            self.request_target_msg.header.frame_id = 'map'
            self.request_target_msg.pose.position.x=self.truck_x
            self.request_target_msg.pose.position.y=self.truck_y
            self.target_publisher.publish(self.request_target_msg)
    
        # 7. 로봇은 목적지에 위치한다. 
        x=self.odom_msg.pose.pose.position.x
        y=self.odom_msg.pose.pose.position.y
        if abs(self.request_target_msg.pose.position.x-x)<=1 and abs(self.request_target_msg.pose.position.y-y)<=1:
            
            # 8. 물건 preview
            self.request_hand_control_msg.control_mode=1        
            self.request_handcontrol_publisher.publish(self.request_hand_control_msg) 
            
            
            # 9. 물건을 내려놓는다.
            self.request_hand_control_msg.control_mode=3        
            self.request_handcontrol_publisher.publish(self.request_hand_control_msg) 
 
            
            # 목적지 주소를 전달한다.
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
    
    
    
        


