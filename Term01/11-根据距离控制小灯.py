import time
import RPi.GPIO as GPIO
LEDs = [5, 6, 12, 16]
Trig_Pin = 20
Echo_Pin = 21
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDs, GPIO.OUT, initial=GPIO.LOW)
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


while True:
    Distance = Ultrasonic_ranging()
    if Distance < 10:
        GPIO.output(LEDs, GPIO.HIGH)
    elif Distance < 20:
        GPIO.output(LEDs[:2], GPIO.HIGH)
        GPIO.output(LEDs[3], GPIO.LOW)
    elif Distance < 30:
        GPIO.output(LEDs[:1], GPIO.HIGH)
        GPIO.output(LEDs[2:], GPIO.LOW)
    elif Distance < 40:
        GPIO.output(LEDs[0], GPIO.HIGH)
        GPIO.output(LEDs[1:3], GPIO.LOW)
    else:
        GPIO.output(LEDs, GPIO.LOW)
    time.sleep(0.2)
