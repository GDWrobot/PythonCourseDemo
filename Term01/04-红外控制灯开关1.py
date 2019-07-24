import RPi.GPIO as GPIO
import time
IR = 24
LED = 16
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(IR, GPIO.IN)  # 设置该端口为输入模式
GPIO.setup(LED, GPIO.OUT)  # 设置该端口为输出模式
while True:
    GPIO.output(LED, GPIO.LOW)
    if GPIO.input(IR) == 0:
        time.sleep(0.3)  # 按键消抖
        while True:
            if GPIO.input(IR) == 0:
                time.sleep(0.3)  # 按键消抖
                break  # 跳出当前循环
            else:
                GPIO.output(LED, GPIO.HIGH)
