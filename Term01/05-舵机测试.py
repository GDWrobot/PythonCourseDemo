import RPi.GPIO as GPIO
import time
servopin = 18  # 舵机接在18号口
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servopin, GPIO.OUT, initial=False)
p = GPIO.PWM(servopin, 50)  # 设置频率为50Hz，周期20ms
p.start(0)
p.ChangeDutyCycle(5)  # 5%，1ms，逆时针转（正转）
time.sleep(2)
p.ChangeDutyCycle(10)  # 10%，2ms，顺时针转（反转）
time.sleep(2)
p.stop()
GPIO.cleanup()  # 清除GPIO占用
