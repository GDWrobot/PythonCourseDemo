import time
import RPi.GPIO as GPIO
import TM1650

button = 25
buzzer = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT, initial=False)
p = GPIO.PWM(buzzer, 500)
digi = TM1650.TM1650()
digi.setBrightness(0, 1)
for i in range(4):
    digi.clearNumber(i)


def displayTimer(secondsleft):
    Min = secondsleft // 60
    Sec = secondsleft % 60
    digi.setNumber(0, Min // 10, 0)
    digi.setNumber(1, Min % 10, 1)
    digi.setNumber(2, Sec // 10, 0)
    digi.setNumber(3, Sec % 10, 0)


Timer = 100

while True:
    displayTimer(Timer)
    for i in range(10):
        if GPIO.input(button):
            Timer = 100
        time.sleep(0.1)
    Timer -= 1
    if Timer % (Timer // 15 + 2) == 0:
        p.start(10)
    else:
        p.stop()
    if Timer < 0:
        break

p.ChangeFrequency(1000)
p.start(10)
time.sleep(3)
p.stop()
GPIO.cleanup()
for i in range(4):
    digi.clearNumber(i)
