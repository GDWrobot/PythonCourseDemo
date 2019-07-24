import RPi.GPIO as GPIO
import time

LEDs = [5, 6, 12, 16]  # 将4个灯的端口号保存在列表里
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDs, GPIO.OUT)  # 可以同时设置列表里所有端口

for n in range(10):  # 重复10次
    for i in range(4):  # 依次点亮4个灯
        GPIO.output(LEDs[i], GPIO.HIGH)  # 使用LEDs[i]访问列表中的值
        time.sleep(0.2)
        GPIO.output(LEDs[i], GPIO.LOW)
