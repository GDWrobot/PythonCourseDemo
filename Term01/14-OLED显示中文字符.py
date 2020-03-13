from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import ImageFont
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=0)
font = ImageFont.truetype("/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc", 20)
# 导入字体文件，20代表字号大小，可以尝试改成其他大小
with canvas(device, dither=False) as draw:
    draw.text((4, 0), "古德微机器人", fill="white", font=font)
