import RPi.GPIO as GPIO
import sys
import time
import pymysql

pin = 18

GPIO.setmode(GPIO.BCM)	# gpio mode setting
GPIO.setup(pin, GPIO.OUT) # motor output
p = GPIO.PWM(pin, 50)
p.start(0)

conn = pymysql.connect(host="192.168.1.102",
			user="dev", passwd="pwd", db="raspberry")

try:
	with conn.cursor() as cur:
		sql = "insert into collect_data values(%s)"

		while True:
			print('servo: 2.5')
			p.ChangeDutyCycle(2.5)
			cur.execute(sql,
				('servo', 2.5))
			conn.commit()

except KeyboardInterrupt :
	exit()
finally :
	conn.close()
