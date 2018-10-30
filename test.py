import math
from egg import *
from utils import *
from actions import Actions
from time import sleep

ADDR_LEFT = 0x04
ADDR_RIGHT = 0x08
ADDR_MEGA = 0x0c
SPD = 60

action = Actions(ADDR_LEFT, ADDR_RIGHT, ADDR_MEGA)

egg_eaten = 0
mission_complete = False
last_target = None

yolo(2)
while not mission_complete:
	target = getTarget()

	if target == None and last_target == None:
		yolo(2)
		continue

	yolo(1)
	if target.cam != 0:
		action.forward(0, 0)
		sleep(0.2)
		last_target = track(target, action)
	
	elif last_target is None:
		last_target = track(target, action)

	elif target is None or last_target.y - 0.1 > target.y:
		print(last_target.y, target.y)
		action.forward(0, 0)
		exit()
		diff = True
		for i in range(5):
			sleep(0.1)
			target = getTarget()

			if target is None:
				continue

			if last_target.y <= target.y:
				diff = False
				last_target = track(target, action)
				break;

		if diff:
			yolo(2)
			action.forward(0, 0)
			sleep(0.5)
			egg_eaten += 1
			last_target = None

	else:
		last_target = track(target, action)

	print(egg_eaten)
	if (egg_eaten == 2):
		action.forward(60, 60)
		sleep(2.5)
		mission_complete = True

	sleep(0.03)
action.forward(0, 0)
