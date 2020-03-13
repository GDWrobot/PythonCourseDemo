from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=0)  # rotate改成1、2、3试试
# 在画布上绘图
with canvas(device, dither=False) as draw:  # dither=True试试
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    draw.text((10, 40), "Hello World", fill="white")
# fill参数修改成其他颜色试试，如red、yellow