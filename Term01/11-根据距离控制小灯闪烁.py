import time
import RPi.GPIO as GPIO

LED = 16
Trig_Pin = 20
Echo_Pin = 21
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT, initial=False)
GPIO.setup(Trig_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Echo_Pin, GPIO.IN)


def Ultrasonic_ranging():
    GPIO.output(Trig_Pin, GPIO.HIGH)  # 发出触发信号
    time.sleep(0.00015)
    GPIO.output(Trig_Pin, GPIO.LOW)
    while GPIO.input(Echo_Pin) != GPIO.HIGH:  # 等待接收高电平
        pass
    t1 = time.time()  # 记录开始时间
    while GPIO.input(Echo_Pin) == GPIO.HIGH:  # 等待高电平结束
        pass
    t2 = time.time()  # 记录结束时间
    distance = (t2 - t1) * 340 * 100 / 2  # 计算距离，单位厘米
    return distance  # 返回结果


p = GPIO.PWM(LED, 0.1)
p.start(20)
while True:
    Distance = Ultrasonic_ranging()
    # 限制范围防止等待过久
    if Distance > 100:
        Distance = 100
    elif Distance < 5:
        Distance = 5
    else:
        p.ChangeFrequency(20 / Distance)
    time.sleep(0.1)
