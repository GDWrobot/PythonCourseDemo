import RPi.GPIO as GPIO
import time

doL,reL,miL,faL,soL,laL,siL=262,294,330,349,392,440,494
do,re,mi,fa,so,la,si=523,587,659,698,784,880,988
doH,reH,miH,faH,soH,laH,siH=1047,1175,1319,1397,1568,1760,1967

music=[do, re, mi, do, do, re, mi, do,
       mi, fa, so, mi, fa, so,
       so, la, so, fa, mi, do, so, la, so, fa, mi, do,
       do, soL, do, do, soL, do]
delay=[0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,
       0.4,0.4,0.8,0.4,0.4,0.8,
       0.3,0.1,0.3,0.1,0.4,0.4,0.3,0.1,0.3,0.1,0.4,0.4,
       0.4,0.4,0.8,0.4,0.4,0.8]

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

p=GPIO.PWM(25, do)
for i in range(len(music)):
    p.ChangeFrequency(music[i])
    p.start(90)
    time.sleep(delay[i])
#    p.stop()
#    time.sleep(0.1)
GPIO.cleanup()