import csv
import math

THRES_DIS_BETWEEN_EGG = 0.1

class Egg():
	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.area = w * h
		self.distance_to_center = math.sqrt(4 * (x - 0.5) ** 2 + 3 * (y - 0.5) ** 2)
		self.distance = self.get_distance()

	def get_distance(self):
		return math.sqrt(self.area) + self.distance_to_center + 0
		
	def print(self):
		print('x:{0} y:{1} weight:{2} height:{3} distance:{4}'.format(self.x, self.y, self.w, self.h, self.distance))

def get_eggs_info(filepath):
	f = open(filepath, 'r')
	row = csv.reader(f, delimiter=',')

	eggs = [Egg(float(r[1]), float(r[2]), float(r[3]), float(r[4])) for r in row]
	f.close()

	return eggs

def get_nearest_egg(eggs):
	neareat_egg = Egg(0, 0, 0.001, 0.001)

	for i in eggs:
		if math.abs(i.distance - neareat_egg.distance) < 0.001:
			if i.distance_to_center < neareat_egg.distance_to_center:
				neareat_egg = i
		elif i.distance < neareat_egg.distance:
			neareat_egg = i

	return neareat_egg

def same_target_egg(egg, last_egg):
	if egg.y < last_egg.y:
		return False
	elif math.sqrt(4 * (egg.x - last_egg.x) ** 2 + 3 * (egg.y - last_egg.y) ** 2) > THRES_DIS_BETWEEN_EGG:
		return False
	else:
		return True
		
