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


def theaterChase(strip, color, wait_ms=50, iterations=10):
    for j in range(iterations):  	# 重复次数，迭代次数
        for q in range(3): 		# 每3个点1组
            for i in range(0, strip.numPixels(), 3):  # 每隔3点处理，亮
                strip.setPixelColor(i + q, color)  # 设置1点的颜色
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):  # 每隔3点处理，灭
                strip.setPixelColor(i + q, 0)


# 调用函数
theaterChase(strip, Color(127, 0, 0), 200, 30)  # 红色彩灯
colorWipe(strip, Color(0, 0, 0), 10)  # 关闭
