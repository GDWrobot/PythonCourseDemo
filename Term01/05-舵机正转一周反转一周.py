import RPi.GPIO as GPIO
import time
servopin = 18  # 舵机接在18号口
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servopin, GPIO.OUT, initial=False)
p = GPIO.PWM(servopin, 50)
p.start(0)
p.ChangeDutyCycle(6)  # 调节速度
time.sleep(1.2)  # 调节时间
p.ChangeDutyCycle(8)
time.sleep(1.3)
p.stop()
GPIO.cleanup()
