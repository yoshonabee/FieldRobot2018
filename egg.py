import csv
import math
import numpy as np

class Egg():
	def __init__(self, cam, x, y, w, h):
		self.cam = cam
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.data = np.array([x, y, w, h]).astype(np.float32)
		
	def print(self):
		print('Cam:{4} x:{0} y:{1} width:{2} height:{3}'.format(self.x, self.y, self.w, self.h, self.cam))

def getTarget():
	f = open('data/egg_info.csv', 'r')
	row = csv.reader(f, delimiter=',')

	eggs = [Egg(int(r[0]), float(r[1]), float(r[2]), float(r[3]), float(r[4])) for r in row]
	f.close()
	
	if len(eggs) == 0:
		return None

	print("\033[2J")
	print("\033[1;1H")

	neareat_egg = None;
	for i in eggs:
		i.print()
		if neareat_egg == None:
			neareat_egg = i

		if (i.y > neareat_egg.y):
			neareat_egg = i

	return neareat_egg
