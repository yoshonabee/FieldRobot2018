import sys
from egg import *
from utils import *
from actions import Actions
from time import sleep

ADDR_LEFT = 0x04
ADDR_RIGHT = 0x08
ADDR_MEGA = 0x0c
SPD = 45

action = Actions(ADDR_LEFT, ADDR_RIGHT, ADDR_MEGA)
move(['r', 'r'], action)
exit()
egg_eaten = int(sys.argv[1])
mission_complete = False
last_target = None

action.forward(45, 45)
sleep(1)

if (len(sys.argv) > 2):
	move(sys.argv[2:], action)

y = yolo(2)
while not mission_complete:
	target = getTarget()

	if target == None and last_target == None:
		y = yolo(2)
		continue

	if y == 2:
		y = yolo(1)
		
		if target.cam != 0:
			action.forward(0, 0)
			sleep(0.2)
			last_target = track(target, action)
	
	elif last_target is None:
		last_target = track(target, action)

	elif target is None or last_target.y - 0.1 > target.y:
		if target is not None:
			print(last_target.y, target.y)
		
		diff = True
		for i in range(5):
			sleep(0.133)
			target = getTarget()

			if target is None:
				continue

			if last_target.y <= target.y:
				diff = False
				last_target = track(target, action)
				break;

		if diff:
			y = yolo(2)
			action.forward(45, 45)
			sleep(0.3)
			egg_eaten += 1
			last_target = None

	else:
		last_target = track(target, action)

	print(egg_eaten)
	if (egg_eaten == 20):
		move(['r', 'r'], action)
		action.forward(60, 60)
		mission_complete = True

	sleep(0.03)
# action.forward(0, 0)
