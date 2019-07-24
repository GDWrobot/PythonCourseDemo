import RPi.GPIO as GPIO
import time

pn = [5, 6, 12, 16, 12, 6]  # 想一想为什么要按这样的顺序？
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pn, GPIO.OUT)

for n in range(10):
    for i in range(6):  # 为什么是6？
        GPIO.output(pn[i], GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(pn[i], GPIO.LOW)
        # time.sleep(0.2)  # 加上后效果有什么变化？
