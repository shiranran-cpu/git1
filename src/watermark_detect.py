import cv2
import numpy as np

def detect_watermark(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # 这里仅做简单检测
    mean_val = np.mean(image)
    if mean_val > 100:
        print("Watermark likely present")
    else:
        print("Watermark likely absent")

if __name__ == "__main__":
    detect_watermark("../data/output.png")
