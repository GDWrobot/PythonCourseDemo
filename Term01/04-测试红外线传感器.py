import RPi.GPIO as GPIO
import time
IR = 24
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(IR, GPIO.IN)  # 设置该端口为输入模式
while True:
    if GPIO.input(IR) == 0:  # 获取该端口读数并判断
        print('IR=0')
    else:
        print('IR=1')  # 有手时是1还是0？
    time.sleep(0.5)
