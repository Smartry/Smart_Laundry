
import time
import MySQLdb
import pymysql
import RPi.GPIO as GPIO
import time
import sys

pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
p = GPIO.PWM(pin, 50)
p.start(0)
cnt = 0
state = 0

conn = pymysql.connect(host="192.168.0.22",user="dev",passwd="pwd",db="ServoDB")

try:
	with conn.cursor() as cur :
		sql="insert into ServoMotor values(%s);"
		while True:
			p.ChangeDutyCycle(10)
			state = 1
			print('Cycle 10')
			cur.execute(sql,(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),state))
			conn.commit()
			time.sleep(1)

			p.ChangeDutyCycle(5)
			state = 0
			print('Cycle 5')
			cur.execute(sql,(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),state))
			conn.commit()
			time.sleep(1)

			p.ChangeDutyCycle(0)
			state = 1
			print('Cycle 0')
			cur.execute(sql,(time.strftime("%y-%m-%d %H:%M:%S",time.localtime()),state))
			conn.commit()
			time.sleep(1)

except KeyboardInterrupt:
	p.stop()

finally:
	conn.close()

GPIO.cleanup()
