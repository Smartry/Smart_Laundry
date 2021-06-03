import time
import RPi.GPIO as io
io.setmode(io.BCM)

door_pin = 6

io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP)

while True:
	if io.input(door_pin):
		print("Door OPEN")
		time.sleep(1.0)
	else:
		print("CLOSE")
		time.sleep(1.0)