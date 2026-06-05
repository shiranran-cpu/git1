import cv2
import numpy as np

def embed_watermark(image_path, watermark_path, output_path):
    image = cv2.imread(image_path)
    watermark = cv2.imread(watermark_path, cv2.IMREAD_UNCHANGED)

    # 简单叠加水印
    h, w = watermark.shape[:2]
    image[0:h, 0:w] = cv2.addWeighted(image[0:h, 0:w], 0.7, watermark, 0.3, 0)

    cv2.imwrite(output_path, image)
    print(f"Watermark embedded: {output_path}")

if __name__ == "__main__":
    embed_watermark("../data/sample_image.png", "../data/sample_image.png", "../data/output.png")
