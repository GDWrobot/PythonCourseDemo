import RPi.GPIO as GPIO
import time
IR = 24
LED = 16
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(IR, GPIO.IN)  # 设置该端口为输入模式
GPIO.setup(LED, GPIO.OUT)  # 设置该端口为输出模式
while True:
    if GPIO.input(IR) == 0:  # 红外有遮挡时小灯亮
        GPIO.output(LED, GPIO.HIGH)
    else:
        GPIO.output(LED, GPIO.LOW)
    time.sleep(0.1)
