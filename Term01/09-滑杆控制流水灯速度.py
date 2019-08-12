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
    feedback = adc.read_adc(0, gain=1)
    delay = 1.0 * feedback / 32767
    GPIO.output(LEDs, GPIO.LOW)
    GPIO.output(LEDs[i], GPIO.HIGH)
    time.sleep(delay)
    i = (i + 1) % 4