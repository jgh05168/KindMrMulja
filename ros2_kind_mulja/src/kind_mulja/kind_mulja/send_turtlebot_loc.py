import socketio
import json
import threading
import rclpy
from rclpy.node import Node
from ssafy_msgs.msg import TurtlebotStatus

class TrutlebotLoc(Node):
    def __init__(self):
        super().__init__('send_turtlebot_loc')
        self.subscription = self.create_subscription(
                TurtlebotStatus,
                'turtlebot_status',
                self.setup_sio,
                10  # QoS profile depth
            )
        self.sio = socketio.Client()
        self.start_msg = False

        self.data = {
            "x": None,
            "y": None,
        }

        # 서버 연결
        @self.sio.event
        def connect():
            print('connection established')
            if not self.start_msg:
                self.sio.emit('sendTime', '터틀봇의 x, y 좌표를 보냅니다. 안녕하세요')
                self.start_msg = True
                
        # 주기적으로 위치를 보내는 타이머 생성
        self.timer = self.create_timer(0.5, self.send_periodic_location)

    def send_location_to_server(self, location_data):
        try:
            '''
            각자 사용하는 로봇 번호에 따라 sendLocation1, sendLocation2, sendLocation3 으로 설정할 것
            - localhost에서 지정해줘야 하므로 무조건 크로스체크 하기(실제 시연하는 로컬에서 설정할 것)
            - camera.py 함수와 같은 number를 사용해야 한다(로봇의 id와 같은 역할)
            '''
            self.sio.emit('sendLocation1', location_data)
            print('Location data sent to server:', location_data)
        except Exception as e:
            print('Failed to send location data to server:', str(e))

    def setup_sio(self, msg):
        self.data["x"] = msg.twist.angular.x
        self.data["y"] = msg.twist.angular.y

    # 주기적으로 위치를 보내는 메소드
    def send_periodic_location(self):
        if self.data["x"] is not None and self.data["y"] is not None:
            # 위치 데이터를 JSON 형태로 변환
            location_data = json.dumps({"x": self.data["x"], "y": self.data["y"]})

            # 서버로 위치 데이터를 전송
            self.send_location_to_server(location_data)

    def start_socketio(self):
        
        # self.sio.connect('https://j10c109.p.ssafy.io/socket')           
        self.sio.connect('https://j10c109.p.ssafy.io')
        # self.sio.connect('http://localhost:12002')
        self.sio.wait()

def main():
    rclpy.init()

    socket_to_location = TrutlebotLoc()
    sio_thread = threading.Thread(target=socket_to_location.start_socketio)
    sio_thread.start()

    rclpy.spin(socket_to_location)
    socket_to_location.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
