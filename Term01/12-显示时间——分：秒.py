import time
import TM1650
digi = TM1650.TM1650()
digi.setBrightness(0, 1)
for i in range(4):
    digi.clearNumber(i)

# 初始化数码管代码省略
while True:
    t = time.localtime()
    digi.setNumber(0, t.tm_min // 10, 0)
    digi.setNumber(1, t.tm_min % 10, 1)
    digi.setNumber(2, t.tm_sec // 10, 0)
    digi.setNumber(3, t.tm_sec % 10, 0)
    time.sleep(0.5)
    digi.setNumber(1, t.tm_min % 10, 0)
    time.sleep(0.5)
