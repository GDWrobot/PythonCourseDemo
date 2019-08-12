import RPi.GPIO as GPIO
import Adafruit_ADS1x15
import time

LEDs = [5, 6, 12, 16]
i = 0
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDs, GPIO.OUT)

adc = Adafruit_ADS1x15.ADS1115()

while True:
    GPIO.output(LEDs, GPIO.LOW)
    GPIO.output(LEDs[i], GPIO.HIGH)
    time.sleep(0.2)
    feedback = adc.read_adc(0, gain=1)
    if feedback < 16000:
        i = (i - 1) % 4
    else:
        i = (i + 1) % 4