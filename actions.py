import smbus
import math

class Actions():
	def __init__(self, mc_addr, ees_addr):
		self.motor_controller = mc_addr
		self.eat_egg_system = ees_addr
		pass
	def turn(self, speed):
		self.motor_controller.write_byte(ord('T'))
		self.motor_controller.write_byte(str(len(str(speed))))
		for s in str(speed):
			self.motor_controller.write_byte(s)
		return

	def forward(self, speed):
		self.motor_controller.write_byte(ord('F'))
		self.motor_controller.write_byte(str(len(str(speed))))
		for s in str(speed):
			self.motor_controller.write_byte(s)
		return

	def eat(self):
		eaten = False

		while not eaten:
			self.motor_controller.write('F1'.format(speed).encode())
			if self.motor_controller.read() == 'E':
				eaten = True
		return
