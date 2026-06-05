# AI Watermark Detection

这是一个用于 AI 生成图像数字水印嵌入与检测的示例项目，演示如何实现可逆水印和篡改检测。

## 目录结构

- `data/` : 样例图像
- `src/` : 核心代码
- `notebooks/` : Jupyter 演示
- `tests/` : 单元测试

## 使用方法

1. 安装依赖：
```bash
pip install -r requirements.txt
2.运行示例：
python src/watermark_detect.py
3.运行测试：
python -m unittest discover tests
