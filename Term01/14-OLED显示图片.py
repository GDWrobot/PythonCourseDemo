from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from PIL import Image
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=0)

img_path = '/home/pi/Downloads/th.jpeg'  # 图片在树莓派上的路径
pic = Image.open(img_path).resize(device.size).convert("RGBA")  # 加载图片
background = Image.new("RGBA", device.size, "white")  # 新建白色背景图片
posn = ((device.width - pic.width) // 2, 0)  # 图片位置居中，也可用(0,0)
background.paste(pic, posn)  # 将图片粘贴到背景上
device.display(background.convert(device.mode))  # 显示背景图片
