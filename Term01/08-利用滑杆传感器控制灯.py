import RPi.GPIO as GPIO
import time
import Adafruit_ADS1x15
LED = 16
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
adc = Adafruit_ADS1x15.ADS1115()
for i in range(200):
    time.sleep(0.1)
    Feedback = adc.read_adc(0, gain=1)
    print(Feedback)
    if Feedback < 10000:
        time.sleep(0.5)
        GPIO.output(LED, GPIO.HIGH)
    else:
        GPIO.output(LED, GPIO.LOW)
