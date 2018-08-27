import smbus
from time import sleep

i2c = smbus.SMBus(1)

ADDR_UNO = 0x04
ADDR_MEGA = 0x08

speed = 0.015

while True:
	i2c.write_i2c_block_data(ADDR_MEGA, 'T', [ord(s) for s in str(speed)])
	# i2c.write_byte(ADDR_MEGA, ord('T'))
	# i2c.write_byte(str(len(str(speed))))
	
	# for s in str(speed):
		# i2c.write_byte(ADDR_MEGA, ord(s))
	
	sleep(1)
