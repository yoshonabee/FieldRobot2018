import serial

class Arduino():
	def __init__(self, port):
		self.port = port
		self.s = serial.Serial(port, 9600)

	def send(self, command):
		s.write(command.encode())
