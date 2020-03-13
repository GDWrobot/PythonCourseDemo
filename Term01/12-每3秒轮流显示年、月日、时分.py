import time
import TM1650
digi = TM1650.TM1650()
digi.setBrightness(0, 1)
for i in range(4):
    digi.clearNumber(i)

# 初始化数码管代码省略


def displayYear(year):
    y = str(year)
    for n in range(4):
        digi.setNumber(n, int(y[n]), 0)


def displayDate(month, day):
    digi.setNumber(0, month // 10, 1)
    digi.setNumber(1, month % 10, 0)
    digi.setNumber(2, day // 10, 0)
    digi.setNumber(3, day % 10, 0)


def displayTime(hour, minute):
    digi.setNumber(0, hour // 10, 0)
    digi.setNumber(1, hour % 10, 1)
    digi.setNumber(2, minute // 10, 0)
    digi.setNumber(3, minute % 10, 0)


while True:
    t = time.localtime()
    displayTime(t.tm_hour, t.tm_min)
    time.sleep(3)
    displayYear(t.tm_year)
    time.sleep(3)
    displayDate(t.tm_mon, t.tm_mday)
    time.sleep(3)