import time
import RPi.GPIO as GPIO

LED = 16
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT, initial=False)
p = GPIO.PWM(LED, 0.5)  # 频率0.5Hz，周期为2s
p.start(30)  # 亮灯时间为0.6s
time.sleep(20)
p.stop()
GPIO.cleanup()
