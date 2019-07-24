import RPi.GPIO as GPIO
import time
servopin = 18  # 舵机接在18号口
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servopin, GPIO.OUT, initial=False)
p = GPIO.PWM(servopin, 50)
p.start(0)
for i in range(5):
    p.ChangeDutyCycle(6)  # 调节速度
    time.sleep(0.38)  # 调节时间，每次转90度
    p.ChangeDutyCycle(7.18)  # 调节占空比让舵机停转
    time.sleep(1)
p.stop()
GPIO.cleanup()
