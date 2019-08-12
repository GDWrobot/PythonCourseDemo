import time
from rpi_ws281x import *  # 导入包
LED_COUNT = 60  # 激活的LED灯数量
LED_PIN = 18  # 灯带端口号
strip = PixelStrip(LED_COUNT, LED_PIN)  # 创建灯带对象
strip.begin()  # 灯带初始化


def colorWipe(strip, color, wait_ms=50):
    """将灯带全部刷成同一颜色"""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)


def wheel(pos):
    """色轮，根据位置返回不同颜色，pos范围0-255"""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)


def rainbow(strip, wait_ms=20, iterations=1):
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)


# 调用
strip.setBrightness(10)  # 调整亮度
rainbow(strip, 5, 10)
colorWipe(strip, Color(0, 0, 0), 10)
