import time
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from PIL import ImageFont, Image, ImageDraw
from weather import weather_now, weather_forecast


def show_time():
    global Time
    Time = time.localtime()
    Date = '{}年{:0>2d}月{:0>2d}日'.format(
        Time.tm_year, Time.tm_mon, Time.tm_mday)
    Clock = '{:0>2d}:{:0>2d}:{:0>2d}'.format(
            Time.tm_hour, Time.tm_min, Time.tm_sec)
    Weekdays = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    background = Image.new("RGBA", device.size, "black")
    ft = ImageFont.truetype("/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc", 17)
    draw = ImageDraw.Draw(background)
    draw.multiline_text((-2, 0), Date+'\n'+Clock+'\n' +
                        Weekdays[Time.tm_wday], fill='white', font=ft, spacing=4, align='center')
    device.display(background.convert(device.mode))


def show_weather_now():
    background = Image.new("RGBA", device.size, "black")
    icon = Image.open(now.cond_icon()).resize((64, 64)).convert("RGBA")
    background.paste(icon, (0, 0))

    ft = ImageFont.truetype("/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc", 18)
    draw = ImageDraw.Draw(background)
    draw.multiline_text((62, 0), now.location() + '\n     ' + now.temperature() +
                        '\n'+now.condition(), fill='white', font=ft, spacing=4, align='right')  # 显示多行文字，注意调整位置、对齐方式、行间距
    device.display(background.convert(device.mode))


def show_weather_forecast(day, day_txt):
    background = Image.new("RGBA", device.size, "black")
    icon = Image.open(forecast.cond_icon(day)).resize((40, 40)).convert("RGBA")
    background.paste(icon, (10, 0))
    ft = ImageFont.truetype("/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc", 18)
    draw = ImageDraw.Draw(background)
    draw.multiline_text((40, 0), day_txt + '\n   ' + forecast.temperature(day) +
                        '\n'+forecast.condition(day), fill='white', font=ft, spacing=4, align='right')
    device.display(background.convert(device.mode))


try:
    now = weather_now()
    forecast = weather_forecast()
    serial = i2c(port=1, address=0x3C)
    device = ssd1306(serial, rotate=0)

    while True:
        for i in range(3):
            show_time()
            time.sleep(1)
        if Time.tm_min % 20 == 0 and Time.tm_sec < 16:
            now = weather_now()
            forecast = weather_forecast()
        show_weather_now()
        time.sleep(3)
        show_weather_forecast(0, '今天')
        time.sleep(3)
        show_weather_forecast(1, '明天')
        time.sleep(3)
        show_weather_forecast(2, '后天')
        time.sleep(3)

except KeyboardInterrupt:
    device.hide()
