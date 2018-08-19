import serial
import math

class Actions():
	def __init__(self, mc_port, ees_port):
		self.motor_controller = serial.Serial(mc_port, 9600)
		self.eat_egg_system = serial.Serial(ees_port, 9600)

	def turn(self, speed):
		self.motor_controller.write('T{0}'.format(speed).encode())
		return

	def forward(self, speed):
		self.motor_controller.write('F{0}'.format(speed).encode())
		return

	def eat(self):
		eaten = False

		while not eaten:
			self.motor_controller.write('F1'.format(speed).encode())
			if self.motor_controller.read() == 'E':
				eaten = True
		return