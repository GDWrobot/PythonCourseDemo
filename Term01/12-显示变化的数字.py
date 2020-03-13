import time
import TM1650

digi = TM1650.TM1650()
digi.setBrightness(0, 1)
for i in range(4):
    digi.clearNumber(i)


def displayNumber(Number):
    s = str(Number)
    for i in range(len(s)):
        digi.setNumber(3-i, int(s[-i-1]), 0)


for n in range(10000):
    displayNumber(n)
    time.sleep(0.2)
