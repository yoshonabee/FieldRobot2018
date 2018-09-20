import math
from egg import *
from utils import get_args
from actions import Actions
from time import sleep

arg = get_args()

THRES_MID = 0.1
STD_SPEED = 45

ADDR_LEFT = 0x04
ADDR_RIGHT = 0x08
ADDR_MEGA = 0x0c

action = Actions(ADDR_LEFT, ADDR_RIGHT, ADDR_MEGA)

egg_eaten = 0
mission_complete = False
last_target = None

action.start();
while not mission_complete:
	eggs = get_eggs_info(arg.eggs_info_filepath)
	
	print("\033[2J")
	print("\033[1;1H")
	for i in eggs:
		i.print()

	target = get_nearest_egg(eggs)
	print('\n\n')
	target.print()

	if last_target is not None:
		if not same_target_egg(target, last_target):
			action.forward(45, 45)
			sleep(5)
			egg_eaten += 1

			if (egg_eaten == 20):
				mission_complete = True

			last_target = None
		else:
			if math.abs(target.x - 0.5) > THRES_MID:
				if target.x > 0.5:
					action.turn(30)
				else:
					action.turn(-30)
			else:
				loss = target.x - 0.5
				action.forward(45 + loss * 5, 45 - loss * 5)

			last_target = target
	else:
		if math.abs(target.x - 0.5) > THRES_MID:
			if target.x > 0.5:
				action.turn(30)
			else:
				action.turn(-30)
		else:
			loss = target.x - 0.5
			action.forward(45 + loss * 5, 45 - loss * 5)

		last_target = target
