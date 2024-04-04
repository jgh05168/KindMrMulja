import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
import cv2
import numpy as np

class CameraSubscriber(Node):
    def __init__(self):
        super().__init__('camera_subscriber')
        self.subscription = self.create_subscription(
            CompressedImage,
            '/image_jpeg/compressed',  # 변경 가능
            self.img_callback,
            10  # QoS profile depth
        )

    def img_callback(self, msg):
        np_arr = np.frombuffer(msg.data, np.uint8)
        cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        # 여기에 카메라 데이터를 가공하는 코드를 추가할 수 있습니다.
        # 예를 들어, 이미지 처리, 딥러닝 모델 적용 등의 작업을 수행할 수 있습니다.
        cv2.imshow('Camera Image', cv_image)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    camera_subscriber = CameraSubscriber()
    rclpy.spin(camera_subscriber)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
