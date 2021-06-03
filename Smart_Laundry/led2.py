import RPi.GPIO as GPIO
import time

pins = [16, 13, 18]

def led_on(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)

    GPIO.output(pin, True)

def led_off(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)

    GPIO.cleanup(pin)

led_on(pins[0])
time.sleep(10)
led_off(pins[0])
time.sleep(10)
led_off(pins[1])
time.sleep(10)
led_off(pins[2])
