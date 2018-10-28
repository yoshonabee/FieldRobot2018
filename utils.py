import math
from egg import *
from actions import Actions
from time import sleep, time

THRES_MID = 0.04
STD_SPEED = 60

def yolo(c):
	f = open('data/command', 'w')
	f.write(str(c)+'\n')
	f.close()
	return


def track(target, action):
	if target.cam != 0:
		if target.cam == 1:
			action.turn(-60)
			sleep(1.5)
		else:
			action.turn(60)
			sleep(1.5)

		target = getTarget()
		while target.cam != 0:
			target = getTarget()
		action.forward(40, 40)
	else:
		loss = target.x - 0.5
		action.forward(STD_SPEED + loss * 50, STD_SPEED - loss * 50)
	return target
