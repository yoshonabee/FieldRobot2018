import smbus
import math

class Actions():
	def __init__(self, mc_addr, ees_addr):
		self.bus = smbus.SMBus(1)
		self.mc = mc_addr
		self.ees = ees_addr
		pass
	def turn(self, speed):
		bus.write_i2c_block_data(self.mc, ord('T'), [ord(s) for s in str(speed)])
		return

	def forward(self, speed):
		bus.write_i2c_block_data(self.mc, ord('F'), [ord(s) for s in str(speed)])
		return

	def eat(self):
		eaten = False

		while not eaten:
			bus.write_i2c_block_data(self.mc, ord('F'), [ord(s) for s in str(speed)])
			if chr(read_byte(self.ees)) == 'E':
				eaten = True
		return
