import math
import torch
# from SE import *
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

action.start();
se = loadModel()

start_time = time()
last_time = start_time

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

	if time() - last_time > 0.1:
		print('time: {0}::{1},{2},{3},{4},{5},{6},{7},{8}'.format(time() - start_time, target.x, target.y, target.w, target.h, last_target.x, last_target.y, last_target.w, last_target.h))
		last_time = time()

	if last_target.y <= target.y:
		last_target = track(target, action)
	else:
		diff = True
		for i in range(5):
			sleep(0.1)
			targets.add(getTarget())

			if target.allNone():
				continue

			target = targets.get()
			if last_target.y <= target:
				diff = False
				last_target = track(target, action)
				break;

		if diff:
			yolo(2)
			sleep(0.07)
			targets.clear()
			last_target = None

	sleep(0.03)
action.forward(0, 0)
