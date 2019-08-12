import RPi.GPIO as GPIO
import time
import Adafruit_ADS1x15
LEDs = [5, 6, 12, 16]
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
adc = Adafruit_ADS1x15.ADS1115()
while True:  # 设置while循环，实现无限循环
    nFeedback = adc.read_adc(0, gain=1)
    print(nFeedback)
    if (nFeedback < 10):  # 判断1，控制灯所有初始状态
        for i in range(4):
            GPIO.output(LEDs[i], GPIO.LOW)
    elif(nFeedback > 10 and nFeedback < 8000):
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(12, GPIO.LOW)
    elif(nFeedback > 8000 and nFeedback < 16000):
        GPIO.output(16, GPIO.LOW)
        GPIO.output(6, GPIO.LOW)
        GPIO.output(12, GPIO.HIGH)
    elif(nFeedback > 16000 and nFeedback < 24000):
        GPIO.output(6, GPIO.HIGH)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(5, GPIO.LOW)
    elif(nFeedback > 24000 and nFeedback < 32767):
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(6, GPIO.LOW)
    else:
        for i in range(4):
            GPIO.output(LEDs[i], GPIO.LOW)
    time.sleep(0.1)
