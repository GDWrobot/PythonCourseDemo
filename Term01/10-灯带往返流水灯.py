import time
from rpi_ws281x import * # 导入包
LED_COUNT = 60 # 激活的LED灯数量
LED_PIN = 18 # 灯带端口号
strip = PixelStrip(LED_COUNT, LED_PIN) # 创建灯带对象
strip.begin() # 灯带初始化

for i in range(strip.numPixels()):
    strip.setPixelColor(i, Color(100, 0, 0))
    strip.show()
    time.sleep(0.05)
    strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()
for i in range(strip.numPixels(), 0, -1):  # 反序
    strip.setPixelColor(i, Color(100, 0, 0))
    strip.show()
    time.sleep(0.05)
    strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()
