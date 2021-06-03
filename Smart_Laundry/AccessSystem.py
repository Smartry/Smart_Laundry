import time

import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO
import requests

import pyzbar.pyzbar as pyzbar
import cv2

servo1 = 19
servo2 = 25

buzzer = 20
led_red = 21
led_green = 13
led_blue = 27
# locker = 27
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
GPIO.setup(servo1, GPIO.OUT)
GPIO.setup(servo2, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(led_red, GPIO.OUT)       # RED
GPIO.setup(led_green, GPIO.OUT)     # GREEN
GPIO.setup(led_blue, GPIO.OUT)      # BLUE
# GPIO.setup(locker, GPIO.OUT)
GPIO.setup(door, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pir, GPIO.IN, GPIO.PUD_UP)

p1 = GPIO.PWM(servo1, 50)
p2 = GPIO.PWM(servo2, 50)
b = GPIO.PWM(buzzer, 262)
p1.start(0)
p2.start(0)

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
# GPIO.output(led_green, 0)   # GREEN OFF
# GPIO.output(led_red, 0)     # RED OFF
# GPIO.output(led_blue, 0)    # BLUE OFF

try:
    while True:
        GPIO.output(led_green, 0)   # GREEN OFF
        GPIO.output(led_red, 0)     # RED OFF
        GPIO.output(led_blue, 0)    # BLUE OFF
        # PIR 
        input_state = GPIO.input(17)

        # Detected
        if input_state == True:                
            GPIO.output(led_green, 1)
            GPIO.output(led_red, 1)
            GPIO.output(led_blue, 1) 
            print("Motion Detected")

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
                # p1.ChangeDutyCycle(2.5)
                # p2.ChangeDutyCycle(2.5)
                # time.sleep(0.5)

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
                
                # GPIO.output(locker, 1)      # LOCKER OPEN
                p1.ChangeDutyCycle(2.5)
                p2.ChangeDutyCycle(7)
                # p2.ChangeDutyCycle(2.5)
                time.sleep(0.5)
                p1.ChangeDutyCycle(6)
                p2.ChangeDutyCycle(2.5)
                # p2.ChangeDutyCycle(9.5)
                time.sleep(0.5)
                # p1.ChangeDutyCycle(6)
                # time.sleep(0.5)
                # GPIO.output(locker, 0)      # LOCKER CLOSE AGAIN

                if GPIO.input(door):        # if door open
                    lcd.message("Door is open")
                    print("Door is open")
                    time.sleep(2.0)
                    lcd.clear()
                    b.start(50.0)
                    time.sleep(1.0)
                    b.stop()
                    # p1.ChangeDutyCycle(2.5)
                    # p2.ChangeDutyCycle(2.5)
                    # time.sleep(0.5)

                else:                       # if door close
                    lcd.message("Door is close")
                    print("Door is close")
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

                # GPIO.output(locker, 0)      # LOCKER CLOSE
                b.start(50.0)
                time.sleep(1.0)
                b.stop()
                p1.ChangeDutyCycle(0)
                p2.ChangeDutyCycle(0)
                time.sleep(0)

            p1.ChangeDutyCycle(0)
            p2.ChangeDutyCycle(0)
            time.sleep(0)

        # No Detection
        else:        
            GPIO.output(led_green, 0)   # GREEN OFF
            GPIO.output(led_red, 0)     # RED OFF
            GPIO.output(led_blue, 0)    # BLUE OFF
            print("No Detection")
            
        GPIO.output(led_green, 0)   # GREEN OFF
        GPIO.output(led_red, 0)     # RED OFF
        GPIO.output(led_blue, 0)    # BLUE OFF
        time.sleep(0.2)

        # # QR Code 
        # cap = cv2.VideoCapture(0)
        # a = ''
        # i = 0

        # while cap.isOpened():
        #     ret, img = cap.read()

        #     if not ret:
        #         continue

        #     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #     decoded = pyzbar.decode(gray)

        #     for d in decoded:
        #         a = d.datar
        #     GPIO.output(led_green, 1)   # GREEN ON
        #     GPIO.output(led_red, 0)     # RED OFF
        #     GPIO.output(locker, 1)      # LOCKER OPEN
        #     p.ChangeDutyCycle(9.5)
        #     time.sleep(0.5)
        #     p.ChangeDutyCycle(2.5)
        #     time.sleep(0.5)
        #     GPIO.output(locker, 0)      # LOCKER CLOSE AGAIN

        #     if GPIO.input(door):        # if door open
        #         lcd.message("Door is open")
        #         time.sleep(2.0)
        #         lcd.clear()
        #         b.start(50.0)
        #         time.sleep(1.0)
        #         b.stop()
        #         p.ChangeDutyCycle(2.5)
        #         time.sleep(0.5)

        #     else:                       # if door close
        #         lcd.message("Door is close")
        #         time.sleep(2.0)
        #         lcd.clear()

        # # Incorrect
        # else:
        #     print("Try again!")
        #     lcd.message("Try again!")   # lcd 'Try again' print
        #     time.sleep(2.0)
        #     lcd.clear()                 # display clear
        #     GPIO.output(led_green, 0)   # GREEN OFF
        #     GPIO.output(led_red, 1)     # RED ON
        #     GPIO.output(locker, 0)      # LOCKER CLOSE
        #     b.start(50.0)
        #     time.sleep(1.0)
        #     b.stop()
        #     p.ChangeDutyCycle(0)
        #     time.sleep(0)

        # p.ChangeDutyCycle(0)
        # time.sleep(0)

except KeyboardInterrupt:
    p1.stop()
    p2.stop()

GPIO.cleanup()
