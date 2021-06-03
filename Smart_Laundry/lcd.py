import time
import Adafruit_CharLCD as LCD

lcd_rs = 26
lcd_en = 24
lcd_d4 = 22
lcd_d5 = 18
lcd_d6 = 16
lcd_d7 = 12
lcd_backlight = 2

lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

print("Hello")
lcd.message('Hello\nworld!')

time.sleep(100.0)
# lcd.clear()
# text = raw_input("Type Something to be displayed: ")
# lcd.message(text)

# time.sleep(2.0)
# lcd.clear()
# print("Bye")
# lcd.message('Goodbye\nWorld!')

# time.sleep(2.0)
# lcd.clear()