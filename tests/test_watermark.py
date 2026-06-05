import unittest
from src.watermark_embed import embed_watermark
from src.watermark_detect import detect_watermark

class TestWatermark(unittest.TestCase):
    def test_embed_and_detect(self):
        embed_watermark("../data/sample_image.png", "../data/sample_image.png", "../data/output.png")
        detect_watermark("../data/output.png")

if __name__ == "__main__":
    unittest.main()
