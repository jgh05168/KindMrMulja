import rclpy
from sensor_msgs.msg import CompressedImage
from ssafy_msgs.msg import BBox
import cv2
import time
import numpy as np
import pytesseract
from PIL import Image

params_cam = {
    "WIDTH": 320,  # image width
    "HEIGHT": 240,  # image height
}

class TextExtractionNode:

    def __init__(self):
        self.node = rclpy.create_node('text_extraction_node')
        self.subscription = self.node.create_subscription(CompressedImage, '/image_jpeg/compressed', self.image_callback, 10)
        self.text_publisher = self.node.create_publisher(BBox, '/text_bbox', 10)
        self.img_bgr = None

    def image_callback(self, msg):
        np_arr = np.frombuffer(msg.data, np.uint8)
        self.img_bgr = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        self.extract_text()

    def extract_text(self):
        if self.img_bgr is not None:
            # Example: Set ROI as the center of the image
            roi_x, roi_y, roi_w, roi_h = 100, 100, 200, 200
            roi_image = self.img_bgr[roi_y:roi_y + roi_h, roi_x:roi_x + roi_w]

            # Convert ROI to grayscale
            gray_roi = cv2.cvtColor(roi_image, cv2.COLOR_BGR2GRAY)

            # Apply thresholding to prepare for OCR
            _, binary_roi = cv2.threshold(gray_roi, 128, 255, cv2.THRESH_BINARY)

            # Use Tesseract OCR to extract text
            text = pytesseract.image_to_string(Image.fromarray(binary_roi))

            # Publish BBox with text information
            bbox_msg = BBox()
            bbox_msg.x = roi_x
            bbox_msg.y = roi_y
            bbox_msg.width = roi_w
            bbox_msg.height = roi_h
            bbox_msg.class_name = text
            self.text_publisher.publish(bbox_msg)

            # Visualize the result (optional)
            cv2.putText(self.img_bgr, text, (roi_x, roi_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2,
                        cv2.LINE_AA)
            cv2.rectangle(self.img_bgr, (roi_x, roi_y), (roi_x + roi_w, roi_y + roi_h), (0, 255, 0), 2)

            # Display the image (optional)
            cv2.imshow('Text Extraction', self.img_bgr)
            cv2.waitKey(1)

    def run(self):
        rclpy.spin(self.node)

if __name__ == '__main__':
    rclpy.init()
    text_extraction_node = TextExtractionNode()
    text_extraction_node.run()
