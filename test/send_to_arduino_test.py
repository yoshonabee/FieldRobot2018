import serial
from time import sleep

plug = 'com'
s = serial.Serial(plug, 9600)


while True:
	s.write('Hello, world!'.encode())
	sleep(1)