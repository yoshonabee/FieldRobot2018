import math
from egg import *
from utils import *
from actions import Actions
from time import sleep, time

ADDR_LEFT = 0x04
ADDR_RIGHT = 0x08
ADDR_MEGA = 0x0c

arg = get_args()

action = Actions(ADDR_LEFT, ADDR_RIGHT, ADDR_MEGA)

egg_eaten = 0
mission_complete = False
last_target = None

# action.start();
while not mission_complete:
	target = getTarget(arg.eggs_info_filepath)
	
	if target == None:
		if last_target = None:
			continue
		else:
			target = last_target

	print("\n\n\n\n")
	target.print()
	continue	
	if last_target is not None:
		if not same_target_egg(target, last_target):
			action.forward(60, 60)
			sleep(5)
			egg_eaten += 1

			if (egg_eaten == 1):
				mission_complete = True

			last_target = None
		else:
			track(target, action)
			last_target = target
	else:
		track(target, action)
		last_target = target

action.forward(0, 0)