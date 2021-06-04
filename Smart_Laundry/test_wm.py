import time

import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO
import requests

import pyzbar.pyzbar as pyzbar
import cv2

buzzer = 20
led_red = 21
led_green = 13
led_blue = 27
door = 6

lcd_rs = 26
lcd_en = 24
lcd_d4 = 22
lcd_d5 = 18
lcd_d6 = 16
lcd_d7 = 12
lcd_backlight = 2

lcd_columns = 16
lcd_rows = 2

start = 7
pause = 8
cos1 = 11
cos2 = 5
temp_up = 17
temp_down = 14
rinse = 19
dry = 23

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(led_red, GPIO.OUT)       # RED
GPIO.setup(led_green, GPIO.OUT)     # GREEN
GPIO.setup(led_blue, GPIO.OUT)      # BLUE
GPIO.setup(door, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(start, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pause, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(cos1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(cos2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(temp_up, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(temp_down, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(rinse, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dry, GPIO.IN, pull_up_down=GPIO.PUD_UP)


b = GPIO.PWM(buzzer, 262)

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

try:
    while True:
        GPIO.output(led_green, 0)   # GREEN OFF
        GPIO.output(led_red, 0)     # RED OFF
        GPIO.output(led_blue, 0)    # BLUE OFF

        # QR Code 
        cap = cv2.VideoCapture(0)
        a = ''
        i = 0

        while cap.isOpened():
            ret, img = cap.read()

            if not ret:
                continue

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            decoded = pyzbar.decode(gray)

            for d in decoded:
                a = d.data

            if len(a) >= 1:
                break
            cv2.imshow('img', img)
            key = cv2.waitKey(1)

        cap.release()
        cv2.destroyAllWindows()
        print(a)

        # Transferring data to server
        data = {'code': a}    
        r = requests.post('http://127.0.0.1:8000/post/', data=data)        

        if GPIO.input(door):        # if door open
            lcd.message("Door is open")
            print("Door is open")
            time.sleep(2.0)
            lcd.clear()
            b.start(50.0)
            time.sleep(1.0)
            b.stop()

        else:                       # if door close
            lcd.message("Door is close")
            print("Door is close")
            time.sleep(2.0)
            lcd.clear()

        # Correct
        if len(a) >= 1:
            print(r.status_code)
            print("Welcome")
            
            lcd.message("Welcome!")     # lcd 'welcome'   
            time.sleep(2.0)
            lcd.clear()                 # display clear
            GPIO.output(led_green, 1)   # GREEN ON
            GPIO.output(led_red, 0)     # RED OFF
            GPIO.output(led_blue, 0)    # BLUE OFF

            if GPIO.input(door):        # if door open
                lcd.message("Door is open")
                print("Door is open")
                GPIO.output(led_green, 0)   # GREEN OFF
                GPIO.output(led_red, 1)     # RED ON
                GPIO.output(led_blue, 0)    # RED OFF
                
                time.sleep(2.0)
                lcd.clear()
                b.start(50.0)
                time.sleep(1.0)
                b.stop()

            else:                       # if door close
                lcd.message("Door is close")
                print("Door is close")
                time.sleep(2.0)
                lcd.clear()

            lcd.message("Push Button")
            print("Push Button")
            time.sleep(2.0)
            lcd.clear()

            while True:
                if not GPIO.input(start):
                    if GPIO.input(door):
                        lcd.message("Door is open")
                        print("Door is open")
                        time.sleep(4.0)
                        GPIO.output(led_green, 0)
                        GPIO.output(led_red, 1)
                        GPIO.output(led_blue, 0)
                        b.start(50.0)
                        time.sleep(1.0)
                        b.stop()
                        time.sleep(2.0)
                    else:
                        lcd.message("Wash start!")
                        print("Wash start!")
                        GPIO.output(led_green, 0)
                        GPIO.output(led_red, 0)
                        GPIO.output(led_blue, 1) 
                        time.sleep(2.0)
                        lcd.clear()
                        break
                elif not GPIO.input(pause):
                    lcd.message("Pause")
                    print("Pause")
                    time.sleep(2.0)
                    lcd.clear()
                elif not GPIO.input(cos1):
                    lcd.message("Course1\n")
                    print("Course1")
                    lcd.message("1:00")
                    print("1:00")
                    time.sleep(2.0)
                    lcd.clear()
                elif not GPIO.input(cos2):
                    lcd.message("Course2\n")
                    print("Course2")
                    lcd.message("1:40")
                    print("1:40")
                    time.sleep(2.0)
                    lcd.clear()
                elif not GPIO.input(temp_up):
                    lcd.message("Temperature Up")
                    print("Temperature Up")
                    time.sleep(2.0)
                    lcd.clear()
                elif not GPIO.input(temp_down):
                    lcd.message("Temperature Down")
                    print("Temperature Down")
                    time.sleep(2.0)
                    lcd.clear()
                elif not GPIO.input(rinse):
                    lcd.message("Add Rinse")
                    print("Add Rinse")
                    time.sleep(2.0)
                    lcd.clear()
                elif not GPIO.input(dry):
                    lcd.message("Add Dry")
                    print("Add Dry")
                    time.sleep(2.0)
                    lcd.clear()
        
        # Incorrect
        else:
            print("Try again!")
            lcd.message("Try again!")   # lcd 'Try again' print
            time.sleep(2.0)
            lcd.clear()                 # display clear
            GPIO.output(led_green, 0)   # GREEN OFF
            GPIO.output(led_red, 1)     # RED ON
            GPIO.output(led_blue, 0)    # RED OFF

            b.start(50.0)
            time.sleep(1.0)
            b.stop()

        time.sleep(0)

        GPIO.output(led_green, 0)   # GREEN OFF
        GPIO.output(led_red, 0)     # RED OFF
        GPIO.output(led_blue, 0)    # BLUE OFF
        time.sleep(0.2)


except KeyboardInterrupt:
    GPIO.output(led_green, 0)   # GREEN OFF
    GPIO.output(led_red, 0)     # RED OFF
    GPIO.output(led_blue, 0)    # BLUE OFF

GPIO.cleanup()
