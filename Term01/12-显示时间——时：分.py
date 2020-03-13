import time
import TM1650
digi = TM1650.TM1650()
digi.setBrightness(0, 1)
for i in range(4):
    digi.clearNumber(i)

while True:
    t = time.localtime()
    digi.setNumber(0, t.tm_hour // 10, 0)  # 时的十位
    digi.setNumber(1, t.tm_hour % 10, 1)  # 时的个位，带点
    digi.setNumber(2, t.tm_min // 10, 0)  # 分的十位
    digi.setNumber(3, t.tm_min % 10, 0)  # 分的个位
    time.sleep(0.5)
