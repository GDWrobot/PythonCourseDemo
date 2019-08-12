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


# 调用函数
colorWipe(strip, Color(255, 0, 0))  # 红色
colorWipe(strip, Color(0, 255, 0), 100)  # 绿色
colorWipe(strip, Color(0, 0, 255), 200)  # 蓝色
colorWipe(strip, Color(0, 0, 0), 10)  # 关闭
