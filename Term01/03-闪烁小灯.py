import RPi.GPIO as GPIO
import time

LED = 16
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

for i in range(20):  # 闪烁20次
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(0.2)  # 0.2秒闪烁
    GPIO.output(LED, GPIO.LOW)
    time.sleep(0.2)
