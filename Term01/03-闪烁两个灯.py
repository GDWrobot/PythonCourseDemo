import RPi.GPIO as GPIO  
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)

for i in range(20):
    GPIO.output(5,GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(5,GPIO.LOW)
    GPIO.output(6,GPIO.HIGH)   
    time.sleep(0.2)
    GPIO.output(6,GPIO.LOW)