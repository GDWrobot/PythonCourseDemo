import time
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=0)

while True:  # 初始化代码已省略
    with canvas(device, dither=False) as draw:
        draw.point([(20, 10), (40, 20), (60, 30), (80, 40)], fill="white")  # 画点
        draw.ellipse([(100, 0), (127, 63)], fill="white", width=3)  # 画椭圆
        draw.polygon([(10, 5), (10, 60), (70, 60)], outline="white")  # 画多边形
    time.sleep(1)
    with canvas(device, dither=False) as draw:
        draw.ellipse([(34, 2), (93, 61)], fill="white")
        draw.line([(63, 30), (63, 40)], fill="black", width=4)
        draw.line([(40, 20), (58, 20)], fill="black", width=3)
        draw.line([(70, 20), (87, 20)], fill="black", width=3)
        draw.arc([(40, 20), (87, 55)], 5, 175, fill="black", width=3)  # 画弧线
    time.sleep(1)
