import RPi.GPIO as GPIO
import time

do=523
re=587
mi=659
fa=698
so=784
la=880
si=988
buzzer = 24
music=[do, do, so, so, la, la, so,
       fa, fa, mi, mi, re, re, do,
       so, so, fa, fa, mi, mi, re,
       so, so, fa, fa, mi, mi, re,
       do, do, so, so, la, la, so,
       fa, fa, mi, mi, re, re, do]
delay=[0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.6,
       0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.6,
       0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.6,
       0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.6,
       0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.6,
       0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)

p=GPIO.PWM(buzzer, do)
for i in range(len(music)):
    p.ChangeFrequency(music[i])
    p.start(90)
    time.sleep(delay[i])
    p.stop()
    time.sleep(0.1)
GPIO.cleanup()