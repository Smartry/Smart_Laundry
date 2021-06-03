import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

for i in range(10):
    GPIO.output(18,0)
    GPIO.output(16,1)
    time.sleep(1)
    print('RED')

    GPIO.output(16,0)
    GPIO.output(13,1)
    time.sleep(1)
    print('GREEN')

    GPIO.output(13,0)
    GPIO.output(18,1)
    time.sleep(1)

    print('BLUE')
GPIO.cleanup()