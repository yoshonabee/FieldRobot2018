from argparse import ArgumentParser
import math
from egg import *
from actions import Actions
from time import sleep, time

THRES_MID = 0.04
STD_SPEED = 60

def yolo(c):
	f = open('command', 'w')
	f.write(str(c)+'\n')
	f.close()
	return


def track(target, action):
	if abs(target.x - 0.5) > THRES_MID:
		if target.x > 0.5:
			action.turn(30)
		else:
			action.turn(-30)
	else:
		loss = target.x - 0.5
		action.forward(STD_SPEED + loss * 5, STD_SPEED - loss * 5)

