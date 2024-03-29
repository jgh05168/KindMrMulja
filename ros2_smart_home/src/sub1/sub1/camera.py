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

    def img_callback(self, msg):
        np_arr = np.frombuffer(msg.data, np.uint8)
        cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        _, img_encoded = cv2.imencode('.jpg', cv_image)
        image_str = img_encoded.tostring()
        
        self.send_image_to_server(image_str)

    def send_image_to_server(self, image_data):
        try:
            self.sio.emit('sendImage', image_data)
            print('Image data sent to server')
        except Exception as e:
            print('Failed to send image data to server:', str(e))

    def start_socketio(self):
        self.sio.connect('http://localhost:12003/')
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
