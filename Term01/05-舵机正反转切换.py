import RPi.GPIO as GPIO
import time
servopin = 18  # 舵机接在18号口
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servopin, GPIO.OUT, initial=False)
p = GPIO.PWM(servopin, 50)
p.start(0)
dc = 5  # 占空比作为变量
for i in range(50):
    dc = 5 + i * 0.1  # 根据循环次数每次变化一点点
    p.ChangeDutyCycle(dc)
    time.sleep(0.5)
p.stop()
GPIO.cleanup()
