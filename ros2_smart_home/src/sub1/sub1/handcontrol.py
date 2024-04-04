import rclpy
from rclpy.node import Node
import os, time
from ssafy_msgs.msg import TurtlebotStatus,HandControl

# Hand Control 노드는 시뮬레이터로부터 데이터를 수신해서 확인(출력)하고, 메세지를 송신해서 Hand Control기능을 사용해 보는 노드입니다. 
# 메시지를 받아서 Hand Control 기능을 사용할 수 있는 상태인지 확인하고, 제어 메시지를 보내 제어가 잘 되는지 확인해보세요. 
# 수신 데이터 : 터틀봇 상태 (/turtlebot_status)
# 송신 데이터 : Hand Control 제어 (/hand_control)


# 노드 로직 순서
# 1. publisher, subscriber 만들기
# 2. 사용자 메뉴 구성
# 3. Hand Control Status 출력
# 4. Hand Control - Preview
# 5. Hand Control - Pick up
# 6. Hand Control - Put down


class Handcontrol(Node):

    def __init__(self):
        super().__init__('hand_control')
                
        ## 로직 1. publisher, subscriber 만들기
        self.hand_control = self.create_publisher(HandControl, '/hand_control', 10)                
        self.turtlebot_status = self.create_subscription(TurtlebotStatus,'/turtlebot_status',self.turtlebot_status_cb,10)

        self.timer = self.create_timer(1, self.timer_callback)
        
        ## 제어 메시지 변수 생성 
        self.hand_control_msg=HandControl()        


        self.turtlebot_status_msg = TurtlebotStatus()
        self.is_turtlebot_status = False
        

    def timer_callback(self):
        # while True:
            # 로직 2. 사용자 메뉴 구성
            print('Select Menu [0: status_check, 1: preview, 2:pick_up, 3:put_down')
            menu=input(">>")
            if menu=='0' :               
                self.hand_control_status()
            if menu=='1' :
                self.hand_control_preview()               
            if menu=='2' :
                self.hand_control_pick_up()   
            if menu=='3' :
                self.hand_control_put_down()


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



 
    def hand_control_preview(self):
   
        if self.is_turtlebot_status:
            print('Entering Preview Mode...')
            
            # Set the control_mode to 1 (Preview)
            self.hand_control_msg.control_mode = 1
            self.hand_control_msg.put_distance = 1.0
            self.hand_control_msg.put_height = 4.0

            timeout = 1  
            start_time = time.time()

            while (time.time() - start_time) < timeout:
        
                    self.hand_control.publish(self.hand_control_msg)
                    time.sleep(0.1)

            print('Preview Mode activated.')
        else:
            print('Waiting for Turtlebot Status...')

        
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
    
        
    def turtlebot_status_cb(self,msg):
        self.is_turtlebot_status=True
        self.turtlebot_status_msg=msg
        

def main(args=None):
    rclpy.init(args=args)
    sub1_hand_control = Handcontrol()    
    rclpy.spin(sub1_hand_control)
    sub1_hand_control.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

