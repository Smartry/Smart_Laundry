import mysql.connector
import RPi.GPIO as GPIO
import time
import datetime
from core import Core
core=Core()

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
servo_PIN = core.gpio

try:
	print "servo Module Test"
	time.sleep(2)
	print "Ready"
	lastval=999;
	dbconnection = core.getDB()
	dbcur = dbconnection.cursor()
	while True:
		nowval=GPIO.input(servo_PIN)
		if(nowval!=lastval):
			lastval=nowval
			logstart=datetime.datetime.now()-datetime.timedelta(seconds=core.logseconds)
			sql = "delete from sensorlog where 'start'<'{}';"
			sql = sql.format(logstart.strftime('%Y-%m-%d %H:%M:%S'))
			sql = "insert into sensorlog ('val','start','end','init')values({},'{}','{}',{});"
			sql = sql.format(nowval,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),1 if lastval==999 else 0)
			dbcur.execute(sql)
			dbconnection.commit()
			print "Changed to "+str(nowval)+"-"+time.strftime('%Y-%m-%d %H:%M:%S')
		time.sleep(0.2)
	except KeyboardInterrupt:
		print "Quit"
		GPIO.cleanup()
