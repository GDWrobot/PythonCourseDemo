import RPi.GPIO as GPIO
import time

doL,reL,miL,faL,soL,laL,siL=262,294,330,349,392,440,494
do,re,mi,fa,so,la,si=523,587,659,698,784,880,988
doH,reH,miH,faH,soH,laH,siH=1047,1175,1319,1397,1568,1760,1967

music=[doH, reH, miH, so, doH, miH, miH, 0,
       reH, doH, reH, soH, soH, soH, soH, 0,
       doH, si, doH, doH, doH, doH, doH, 0,
       si, doH, si, doH, si, la, so, 0,
       so, so, la, la, la, la, la, 0,
       so, mi, so, mi, so, reH, doH, 0,
       so, miH, miH, miH, faH, soH, doH, doH, reH, miH, reH, 0]
delay=[0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 
       0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 
       0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 
       0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2,
       0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2,
       0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.4, 0.2,
       0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.1, 0.1, 1.2, 0.4]

LEDs = [5, 6, 12, 16, 25, 21, 24]
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(20, GPIO.OUT, initial = False)
GPIO.setup(LEDs, GPIO.OUT, initial = GPIO.LOW)

p=GPIO.PWM(20, do)

for i in range(len(music)):
    p.start(50)
    if music[i] == do or music[i] == doL or music[i] == doH:
        GPIO.output(LEDs[0], GPIO.HIGH)
    if music[i] == re or music[i] == reL or music[i] == reH:
        GPIO.output(LEDs[1], GPIO.HIGH)
    if music[i] == mi or music[i] == miL or music[i] == miH:
        GPIO.output(LEDs[2], GPIO.HIGH)
    if music[i] == fa or music[i] == faL or music[i] == faH:
        GPIO.output(LEDs[3], GPIO.HIGH)
    if music[i] == so or music[i] == soL or music[i] == soH:
        GPIO.output(LEDs[4], GPIO.HIGH)
    if music[i] == la or music[i] == laL or music[i] == laH:
        GPIO.output(LEDs[5], GPIO.HIGH)
    if music[i] == si or music[i] == siL or music[i] == siH:
        GPIO.output(LEDs[6], GPIO.HIGH)
    if music[i] == 0:
        p.stop()
        GPIO.output(LEDs, GPIO.LOW)
    else:
        p.ChangeFrequency(music[i])
    time.sleep(delay[i])
    GPIO.output(LEDs, GPIO.LOW)
    p.stop()
    time.sleep(0.05)
p.stop()
GPIO.cleanup()