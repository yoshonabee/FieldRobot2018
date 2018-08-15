import serial
from time import sleep

plug = '/dev/cu.usbmodem1411'
s = serial.Serial(plug, 9600)


while True:
	s.write('H'.encode())
	sleep(1)
	s.write('L'.encode())
	sleep(1)