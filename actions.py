import smbus

class Actions():
	def __init__(self, mc_addr, ees_addr):
		self.bus = smbus.SMBus(1)
		self.left = left_addr
		self.right = right_addr
		self.ees = ees_addr

	def forward(self, speed):
		bus.write_i2c_block_data(self.left, ord('F'), [ord(s) for s in str(speed)])
		bus.write_i2c_block_data(self.right, ord('F'), [ord(s) for s in str(speed)])
		return

	def backward(self, speed):
		bus.write_i2c_block_data(self.left, ord('B'), [ord(s) for s in str(speed)])
		bus.write_i2c_block_data(self.right, ord('B'), [ord(s) for s in str(speed)])
		return

	def turn(self, speed):
		if speed >= 0:
			bus.write_i2c_block_data(self.left, ord('F'), [ord(s) for s in str(speed)])
			bus.write_i2c_block_data(self.right, ord('B'), [ord(s) for s in str(speed)])
		else:
			bus.write_i2c_block_data(self.left, ord('B'), [ord(s) for s in str(speed)])
			bus.write_i2c_block_data(self.right, ord('F'), [ord(s) for s in str(speed)])
		return

	

	def eat(self):
		eaten = False

		while not eaten:
			bus.write_i2c_block_data(self.mc, ord('F'), [ord(s) for s in '15'])
			if chr(read_byte(self.ees)) == 'E':
				eaten = True
		return
