import math
from egg import *
from actions import Actions
from time import sleep

THRES_MID = 0.04
STD_SPEED = 60
TD = 40
TURN = 1
FORWARD = 1.8
L_FORWARD = 58 / 43 * FORWARD

def yolo(c):
	f = open('data/command', 'w')
	f.write(str(c)+'\n')
	f.close()
	return c


def track(target, action):
	if target.cam != 0:
		if target.cam == 1:
			action.turn(60)
			sleep(target.x)
		else:
			action.turn(-60)
			sleep(1 - target.x)

		target = getTarget()
		while target is None:
			target = getTarget()

	loss = target.x - 0.5
	action.forward(STD_SPEED + loss * TD, STD_SPEED - loss * TD)
	return target

def move(M, action):
	for m in M:
		if m == 'r':
			action.turn(60)
			sleep(TURN)
		elif m == 'l':
			action.turn(-60)
			sleep(TURN)
		elif m == 'b':
			action.forward(60, 60)
			sleep(L_FORWARD)
		else:
			action.forward(60, 60)
			sleep(float(m) * FORWARD)

