import time
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import ImageFont
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=0)
font = ImageFont.truetype("/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc", 17)

Weekdays = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
while True:
    Time = time.localtime()
    Date = '{}年{:0>2d}月{:0>2d}日'.format(
        Time.tm_year, Time.tm_mon, Time.tm_mday)
    Clock = '{:0>2d}:{:0>2d}:{:0>2d}'.format(
        Time.tm_hour, Time.tm_min, Time.tm_sec)
    with canvas(device, dither=False) as draw:
        draw.text((-2, 2), Date, fill="white", font=font)
        draw.text((40, 23), Weekdays[Time.tm_wday], fill="white", font=font)
        draw.text((30, 44), Clock, fill="white", font=font)
    time.sleep(1)
