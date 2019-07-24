import RPi.GPIO as GPIO
import time
IR = 24
servopin = 18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(IR, GPIO.IN)
GPIO.setup(servopin, GPIO.OUT, initial=False)
p = GPIO.PWM(servopin, 50)
p.start(0)
flag = 0
speed = [5, 7.5, 10, 7.5]
for i in range(50):
    time.sleep(0.2)
    if GPIO.input(IR) == 0:
        time.sleep(0.3)
        flag = (flag + 1) % 4
    p.ChangeDutyCycle(speed[flag])
p.stop()
GPIO.cleanup()
