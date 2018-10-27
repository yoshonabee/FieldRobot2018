import math
import torch
from SE import *
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

# action.start();
se = loadModel()

start_time = time.time()
last_time = start_time

while not mission_complete:
	targets.add(getTarget())
	
	if targets.allNone():
		yolo(3)
		action.forward(SPD, SPD)
		continue

	target = targets.get()
	
	if time.time() - last_time > 0.1:
		print('time: {0}::{1},{2},{3},{4},{5},{6},{7},{8}'.format(time.time() - start_time), target.x, target.y, target.w, target.h, last_target.x, last_target.y, last_target.w, last_target.h)
		last_time = time.time()

	same_egg = result(se(mergeData(target.data, last_target.data)))

	if same_egg:
		track(target)
	else:
		for i in range(5):
			sleep(0.1)
			targets.add(getTarget())
			target = targets.get()
			if result(se(mergeData(target, last_target.data))):
				track(target)
				break;

		action.forward(0, 0)


	last_target = target
action.forward(0, 0)
