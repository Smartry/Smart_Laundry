import time

import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO
import requests

import pandas as pd

servo = 19
buzzer = 20
led_red = 21
led_green = 13
locker = 27
door = 6
pir = 17

lcd_rs = 26
lcd_en = 24
lcd_d4 = 22
lcd_d5 = 18
lcd_d6 = 16
lcd_d7 = 12
lcd_backlight = 2

lcd_columns = 16
lcd_rows = 2

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(led_red, GPIO.OUT)       # RED
GPIO.setup(led_green, GPIO.OUT)     # GREEN
GPIO.setup(locker, GPIO.OUT)
GPIO.setup(door, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pir, GPIO.IN, GPIO.PUD_UP)

p = GPIO.PWM(servo, 50)
b = GPIO.PWM(buzzer, 262)
p.start(0)

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

# print(df)
try:
    while True:
        # if GPIO.input(pir) == True:
        #     print("Motion Detected")
        # else:
        #     print("No Detection")
        #     time.sleep(0.2)

        df = pd.read_csv('/home/pi/Smart_Laundry/QR_Code/barcodes.csv')
        a = df.iloc[-1][1]
        print(a)
        # c = a.loc[1]
        # print(c)

        key = raw_input("Enter Y/N : ")
        data = {'servo': key, 'code': a}
        # r = requests.post('http://127.0.0.1:8000/post/', data={'servo': key, 'code': c})        
        r = requests.post('http://127.0.0.1:8000/post/', data=data)        

        if key.upper() == 'Y':
            print(r.status_code)
            print("Welcome")

            lcd.message("Welcome!")     # lcd 'welcome'   
            time.sleep(2.0)
            lcd.clear()                 # display clear
            GPIO.output(led_green, 1)   # GREEN ON
            GPIO.output(led_red, 0)     # RED OFF
            GPIO.output(locker, 1)      # LOCKER OPEN
            # p.ChangeDutyCycle(9.5)
            # p.ChangeDutyCycle(2.5)
            # time.sleep(0.5)
            p.ChangeDutyCycle(2.5)
            time.sleep(0.5)
            print("1")
            p.ChangeDutyCycle(6)
            time.sleep(0.5)
            print("2")
            # p.ChangeDutyCycle(2.5)
            # time.sleep(0.5)
            # print("3")
            GPIO.output(locker, 0)      # LOCKER CLOSE AGAIN

            if GPIO.input(door):        # if door open
                lcd.message("Door is open")
                time.sleep(2.0)
                lcd.clear()
                b.start(50.0)
                time.sleep(1.0)
                b.stop()
                # p.ChangeDutyCycle(2.5)
                # time.sleep(0.5)

            else:                       # if door close
                lcd.message("Door is close")
                time.sleep(2.0)
                lcd.clear()

        if key.upper() == 'N':
            print("Try again!")
            lcd.message("Try again!")   # lcd 'Try again' print
            time.sleep(2.0)
            lcd.clear()                 # display clear
            GPIO.output(led_green, 0)   # GREEN OFF
            GPIO.output(led_red, 1)     # RED ON
            GPIO.output(locker, 0)      # LOCKER CLOSE
            b.start(50.0)
            time.sleep(1.0)
            b.stop()
            p.ChangeDutyCycle(0)
            time.sleep(0)

        p.ChangeDutyCycle(0)
        time.sleep(0)

except KeyboardInterrupt:
    p.stop()


GPIO.cleanup()
