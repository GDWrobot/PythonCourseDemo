import RPi.GPIO as GPIO
import time
do, re, mi, fa, so, la, si = 523, 587, 659, 698, 784, 880, 988
buzzer = 24  # 蜂鸣器在24号口
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT, initial=False)
p = GPIO.PWM(buzzer, do)
p.start(10)
p.ChangeFrequency(do)
time.sleep(1)
p.ChangeFrequency(mi)  # 试试修改成不同音调
time.sleep(1)
p.stop()
GPIO.cleanup()
