import RPi.GPIO as GPIO
import time
IR = 24
pn = [5, 6, 12, 16, 12, 6]
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(IR, GPIO.IN)
GPIO.setup(pn, GPIO.OUT)
led = 0
while True:
    if GPIO.input(IR) == 0:
        time.sleep(0.3)
        led = (led + 1) % 2
    if led == 1:
        for i in range(6):
            GPIO.output(pn[i], GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(pn[i], GPIO.LOW)
            if GPIO.input(IR) == 0:
                break
