from egg import *
from utils import *
from actions import Actions
from time import time, sleep

ADDR_LEFT = 0x04
ADDR_RIGHT = 0x08
ADDR_MEGA = 0x0c
SPD = 60
TD = 30

I = 13
C1 = 11
C2 = 7.7
C3 = 5.5
C4 = 7.5
C5 = 6
C6 = 4.5
C7 = 3
C8 = 1.5


action = Actions(ADDR_LEFT, ADDR_RIGHT, ADDR_MEGA)

yolo(1)
road = [I, C1, C1, C2, C2, C3, C3, C4, C4, C5, C5, C6, C6, C7, C7, C8]


for r in road:
	start = time()
	while time() - start < r:
		target = getTarget()

		if target is not None:
			if target.x > 0.40 and target.x < 0.60:
				loss = (target.x - 0.5) * TD
				action.forward(SPD + loss, SPD - loss)
		else:
			action.forward(SPD, SPD)

	action.turn(60)
	sleep(1)

action.forward(0, 0)
