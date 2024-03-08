import rclpy
from rclpy.node import Node
from ssafy_msgs.msg import RequestHandControl

class request_handcontrol(Node):
    def __init__(self):
        super().__init__('hand_control')
                
        ## 로직 1. publisher, subscriber 만들기
        self.request_handcontrol_publisher=self.create_publisher(RequestHandControl,'/request_handcontrol',10)
        
                      
        self.timer = self.create_timer(1, self.timer_callback)
        
        ## 제어 메시지 변수 생성 
        self.request_hand_control_msg=RequestHandControl()   
        
    def timer_callback(self):
        # while True:
            # 로직 2. 사용자 메뉴 구성
            print('Select Menu [0: status_check, 1: preview, 2:pick_up, 3:put_down]')
            menu=input(">>")
            if menu=='0' :    
                self.request_hand_control_msg.control_mode=0           
                self.request_handcontrol_publisher.publish(self.request_hand_control_msg)
            if menu=='1' :
                self.request_hand_control_msg.control_mode=1          
                self.request_handcontrol_publisher.publish(self.request_hand_control_msg)
                             
            if menu=='2' :
                self.request_hand_control_msg.control_mode=2           
                self.request_handcontrol_publisher.publish(self.request_hand_control_msg)
                  
            if menu=='3' :
                self.request_hand_control_msg.control_mode=3           
                self.request_handcontrol_publisher.publish(self.request_hand_control_msg)
                
def main(args=None):
    rclpy.init(args=args)
    sub2_request_hand_control = request_handcontrol()    
    rclpy.spin(sub2_request_hand_control)
    sub2_request_hand_control.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
                  
