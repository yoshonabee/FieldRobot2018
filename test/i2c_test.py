import smbus
import time
# for RPI version 1, use "bus = smbus.SMBus(0)"
i2c = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
ADDR_UNO = 0x04
ADDR_MEGA = 0x08

for i in range(100)
	if i % 2 == 1:
		i2c.write_byte(ADDR_UNO, i)
	else:
		i2c.write_byte(ADDR_MEGA, i)
	time.sleep(0.5)