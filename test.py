import math
from egg import *
from utils import *
from actions import Actions
from time import sleep, time
from que import Queue

ADDR_LEFT = 0x04
ADDR_RIGHT = 0x08
ADDR_MEGA = 0x0c
SPD = 60

action = Actions(ADDR_LEFT, ADDR_RIGHT, ADDR_MEGA)

egg_eaten = 0
mission_complete = False
last_target = None

targets = Queue(5)

#action.start();
#se = loadModel()

start_time = time()
last_time = start_time
yolo(2)
while not mission_complete:
	targets.add(getTarget())
	
	if targets.allNone():
		yolo(2)
		action.forward(SPD, SPD)
		continue

	target = targets.get()
	yolo(1)
	
	if target.cam != 0:
		action.forward(0, 0)
		sleep(0.2)
		last_target = track(target, action)
	
	if last_target is None:
		last_target = target
		sleep(0.03)
		continue

	if last_target.y <= target.y:
		last_target = track(target, action)
	else:
		diff = True
		for i in range(5):
			sleep(0.1)
			targets.add(getTarget())

			if targets.allNone():
				continue

			target = targets.get()
			if last_target.y <= target.y:
				diff = False
				last_target = track(target, action)
				break;

		if diff:
			yolo(2)
			action.forward(0, 0)
			sleep(0.5)
			egg_eaten += 1
			targets.clear()
			last_target = None
	print(egg_eaten)
	if (egg_eaten == 2):
		action.forward(60, 60)
		sleep(2.5)
		mission_complete = True

	sleep(0.03)
action.forward(0, 0)
