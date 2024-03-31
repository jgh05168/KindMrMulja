import rclpy
from rclpy.node import Node
import time
from ssafy_msgs.msg import TurtlebotStatus,HandControl,RequestHandControl

# 수신 데이터 : 터틀봇 상태 (/turtlebot_status), 물건 명령 (/request_handcontrol)
# 송신 데이터 : Hand Control 제어 (/hand_control)

# 노드 로직 순서 
# 1. publisher, subscriber 만들기
# 2 Hand Control Status 출력
# 3. Hand Control - Preview
# 4. Hand Control - Pick up
# 5. Hand Control - Put down

class AutoHandcontrol(Node):

    def __init__(self):
        super().__init__('hand_control')
                
        ## 로직 1. publisher, subscriber 만들기, “queue size” is 10
        self.hand_control = self.create_publisher(HandControl, '/hand_control', 10)                
        self.turtlebot_status = self.create_subscription(TurtlebotStatus,'/turtlebot_status',self.turtlebot_status_cb,10)      
        # request_handcontrol subscriber
        self.request_handcontrol=self.create_subscription(RequestHandControl,'/request_handcontrol',self.request_handcontrol_cb,10)
        
        ## 제어 메시지 변수 생성 
        self.hand_control_msg=HandControl()        

        self.turtlebot_status_msg = TurtlebotStatus()
        self.is_turtlebot_status = False
        
        # handcontrol 명령 메세지 
        self.request_handcontrol_msg=RequestHandControl()
        self.is_request_handcontrol_status=False
        
        
    def turtlebot_status_cb(self,msg):
        self.is_turtlebot_status=True
        self.turtlebot_status_msg=msg
        
    # handcontrol subscriber callback 
    def request_handcontrol_cb(self,msg):
        self.is_request_handcontrol_status=True
        self.request_handcontrol_msg=msg
        
        # msg control_mode 번호에 따라 아래 함수 호출 
        if self.request_handcontrol_msg.control_mode==0:
            self.hand_control_status()
        elif self.request_handcontrol_msg.control_mode==1:
            self.hand_control_preview()
        elif self.request_handcontrol_msg.control_mode==2:
            self.hand_control_pick_up()
        elif self.request_handcontrol_msg.control_mode==3:
            self.hand_control_put_down()
            
            
    # 현재 hand_control 상태 확인
    def hand_control_status(self):
        
        # Read Hand Control status
        control_mode = self.hand_control_msg.control_mode
        
        # Display status accordingly
        if control_mode == 1:
            print('Current Status: Preview Mode')
        elif control_mode == 2:
            print('Current Status: Pick Up Mode')
        elif control_mode == 3:
            print('Current Status: Put Down Mode')
        else:
            print('Unknown Status:', control_mode)
            

    # hand control pick_up 상태 
    def hand_control_pick_up(self):
        if self.is_turtlebot_status:
            if self.turtlebot_status_msg.can_lift:
                print('Executing Pick Up...')
                
                self.hand_control_msg.control_mode = 2
                
                timeout = 1  
                start_time = time.time()
                
                while self.turtlebot_status_msg.can_lift and (time.time() - start_time) < timeout:
        
                    self.hand_control.publish(self.hand_control_msg)
                    time.sleep(0.1)

                print('Pick Up completed.')
               
            else:
                print('Robot cannot lift at the moment.')
        else:
            print('Waiting for Turtlebot Status...')



    # hand control preview 상태 
    def hand_control_preview(self):
   
        if self.is_turtlebot_status:
            print('Entering Preview Mode...')
            
            # Set the control_mode to 1 (Preview)
            self.hand_control_msg.control_mode = 1
            self.hand_control_msg.put_distance = 1.0
            self.hand_control_msg.put_height = 0.8

            timeout = 1  
            start_time = time.time()

            while (time.time() - start_time) < timeout:
        
                    self.hand_control.publish(self.hand_control_msg)
                    time.sleep(0.1)

            print('Preview Mode activated.')
        else:
            print('Waiting for Turtlebot Status...')

    # hand control put_down 상태 
    def hand_control_put_down(self):
    
        if self.is_turtlebot_status:

            if self.turtlebot_status_msg.can_put:
                
                self.hand_control_msg.control_mode = 3
                timeout = 1  
                start_time = time.time()
                
                while self.turtlebot_status_msg.can_put and (time.time() - start_time) < timeout:
        
                    self.hand_control.publish(self.hand_control_msg)
                    time.sleep(0.1)

                print('Put Down completed.')
            else:
                print('Robot cannot put down at the moment.')
        else:
            print('Waiting for Turtlebot Status...')
            
def main(args=None):
    rclpy.init(args=args)
    sub1_hand_control = AutoHandcontrol()    
    rclpy.spin(sub1_hand_control)
    sub1_hand_control.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()