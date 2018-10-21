from argparse import ArgumentParser
import math
from egg import *
from actions import Actions
from time import sleep, time

THRES_MID = 0.1
STD_SPEED = 45

def get_args():
	parser = ArgumentParser(prog='python3 fieldRobot.py')

	parser.add_argument('eggs_info_filepath', help='positional argument 1')
	parser.add_argument('-r', '--optional-arg', help='numbers of remain eggs', dest='remain', default=None)

	# parser.print_help()

	return parser.parse_args()

def track(target, action):
	if math.abs(target.x - 0.5) > THRES_MID:
		if target.x > 0.5:
			action.turn(30)
		else:
			action.turn(-30)
	else:
		loss = target.x - 0.5
		action.forward(STD_SPEED + loss * 5, STD_SPEED - loss * 5)

