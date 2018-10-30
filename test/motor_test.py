import smbus
from time import sleep

bus = smbus.SMBus(1)

ADDR_LEFT = 0x04
ADDR_RIGHT = 0x08

# speed = 45

# while True:
bus.write_i2c_block_data(ADDR_LEFT, ord('B'), [ord(s) for s in str(60)])
bus.write_i2c_block_data(ADDR_RIGHT, ord('F'), [ord(s) for s in str(60)])
print(60, 60)
sleep(1)
bus.write_i2c_block_data(ADDR_LEFT, ord('F'), [ord(s) for s in str(0)])
bus.write_i2c_block_data(ADDR_RIGHT, ord('F'), [ord(s) for s in str(0)])
