import smbus

class Actions():
	def __init__(self, left_addr, right_addr, ees_addr):
		self.bus = smbus.SMBus(1)
		self.left = left_addr
		self.right = right_addr
		self.ees = ees_addr

	def start():
		self.bus.write_byte(self.ees, ord('1'));

	def forward(self, spd_left, spd_right):
		self.bus.write_i2c_block_data(self.left, ord('F'), [ord(s) for s in str(spd_left)])
		self.bus.write_i2c_block_data(self.right, ord('F'), [ord(s) for s in str(spd_right)])
		return

	def backward(self, spd_left, spd_right):
		self.bus.write_i2c_block_data(self.left, ord('B'), [ord(s) for s in str(spd_left)])
		self.bus.write_i2c_block_data(self.right, ord('B'), [ord(s) for s in str(spd_right)])
		return

	def turn(self, spd):
		if spd >= 0:
			self.bus.write_i2c_block_data(self.left, ord('F'), [ord(s) for s in str(spd)])
			self.bus.write_i2c_block_data(self.right, ord('B'), [ord(s) for s in str(spd)])
		else:
			self.bus.write_i2c_block_data(self.left, ord('B'), [ord(s) for s in str(spd)])
			self.bus.write_i2c_block_data(self.right, ord('F'), [ord(s) for s in str(spd)])
		return
