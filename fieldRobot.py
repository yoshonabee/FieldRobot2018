import math
from egg import *
from utils import get_args
from actions import Actions

arg = get_args()

THRES_MID = 0.05
ARDUINO_MEGA_PORT = 'mega'
ARDUINO_UNO_PORT = 'uno'

action = Actions(ARDUINO_MEGA_PORT, ARDUINO_UNO_PORT)

egg_eaten = 0
mission_complete = False
last_target = None

while not mission_complete:
	eggs = get_eggs_info(arg.eggs_info_filepath)
	
	print("\033[2J")
	print("\033[1;1H")
	for i in eggs:
		print('x:{0} y:{1} w:{2} h:{3}'.format(i.x, i.y, i.w, i.h))
	continue

	target = get_nearest_egg(eggs)

	if last_target is not None:
		if not same_target_egg(target, last_target):
			action.eat()
			egg_eaten += 1
	else:
		if math.abs(target.x - 0.5) > THRES_MID:
			action.turn(target.x - 0.5)
		else:
			action.forward(1)

	if (egg_eaten == 20):
		mission_complete = True

	last_target = target