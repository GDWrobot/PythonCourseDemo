import RPi.GPIO as GPIO  # 导入模块，#号后代表注释
import time
# 对使用的GPIO端口进行初始化
LED = 16
GPIO.setwarnings(False)  # 模块内置功能，一般要加上
GPIO.setmode(GPIO.BCM)  # 设置GPIO引脚为BCM编码模式
GPIO.setup(LED, GPIO.OUT)  # 设置该端口为输出模式
# 点亮小灯
GPIO.output(LED, GPIO.HIGH)  # 输出高电平（数字信号1）
time.sleep(1)  # 延时1秒
GPIO.output(LED, GPIO.LOW)  # 输出低电平（数字信号0）
