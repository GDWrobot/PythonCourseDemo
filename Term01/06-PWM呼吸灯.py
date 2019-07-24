import time
import RPi.GPIO as GPIO

LED = 16
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT, initial=False)
p = GPIO.PWM(LED, 50)
p.start(0)
for i in range(10):
    for dc in range(0, 101, 5):
        p.ChangeDutyCycle(dc)
        time.sleep(0.1)
    for dc in range(100, -1, -5):
        p.ChangeDutyCycle(dc)
        time.sleep(0.1)
p.stop()
GPIO.cleanup()
