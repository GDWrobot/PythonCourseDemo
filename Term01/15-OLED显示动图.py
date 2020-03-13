import time
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from PIL import Image, ImageSequence
from luma.core.sprite_system import framerate_regulator

serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=0)
regulator = framerate_regulator(fps=20)  # 设置gif播放帧率
img_path = '/home/pi/Desktop/1.gif'
gif = Image.open(img_path)
size = [128, 64]
posn = (0, 0)
while True:
    for frame in ImageSequence.Iterator(gif):  # 每次显示一帧
        with regulator:
            background = Image.new("RGB", device.size, "white")
            background.paste(frame.resize(size, resample=Image.LANCZOS), posn)
            device.display(background.convert(device.mode))
            time.sleep(0.05)  # 等待时间为设置的fps的倒数
