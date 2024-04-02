import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
import cv2
import numpy as np
import socketio
import threading

class CameraSubscriber(Node):
    def __init__(self):
        super().__init__('camera_subscriber')
        self.subscription = self.create_subscription(
            CompressedImage,
            '/image_jpeg/compressed',  # 변경 가능
            self.img_callback,
            10  # QoS profile depth
        )
        self.sio = socketio.Client()
        self.start_msg = False
        
        # 서버 연결
        @self.sio.event
        def connect():
            print('connection established')
            if not self.start_msg:
                self.sio.emit('sendTime', '터틀봇의 카메라 정보를 보냅니다. 안녕하세요')
                self.start_msg = True

    def img_callback(self, msg):
        np_arr = np.frombuffer(msg.data, np.uint8)
        cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        _, img_encoded = cv2.imencode('.jpg', cv_image)
        image_str = img_encoded.tostring()
        
        self.send_image_to_server(image_str)


    def send_image_to_server(self, image_data):
        try:
            self.sio.emit('sendImage1', image_data)
            # print(image_data)
            print('Image data sent to server')
        except Exception as e:
            print('Failed to send image data to server:', str(e))


    def start_socketio(self):
        '''
        각자 사용하는 로봇 번호에 따라 /socket1, /socket2, /socket3 으로 설정할 것
        - localhost에서 지정해줘야 하므로 무조건 크로스체크 하기(실제 시연하는 로컬에서 설정할 것)
        - camera.py 함수와 같은 number를 사용해야 한다(로봇의 id와 같은 역할)
        '''
        # self.sio.connect('https://j10c109.p.ssafy.io/socket1')
        # self.sio.connect('http://localhost:12002')
        self.sio.connect('https://j10c109.p.ssafy.io')
        self.sio.wait()

def main():
    rclpy.init()

    camera_subscriber = CameraSubscriber()
    sio_thread = threading.Thread(target=camera_subscriber.start_socketio)
    sio_thread.start()

    rclpy.spin(camera_subscriber)
    camera_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
