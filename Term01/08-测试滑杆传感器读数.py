import time
import Adafruit_ADS1x15  # 引用模数转换器第三方库包
adc = Adafruit_ADS1x15.ADS1115()  # 生成模数转换器具体实例
for i in range(200):
    time.sleep(0.1)
    Feedback = adc.read_adc(0, gain=1)
    # 从A0串口读取滑杆位置一个读数
    print(Feedback)
