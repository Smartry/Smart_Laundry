import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

while True:
    input_state = GPIO.input(17)
    if input_state == True:
        print("Motion Detected")
    else:
        print("No Detection")
    time.sleep(0.2)
    