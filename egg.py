import csv

class Egg():
	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.distance = self.get_distance(x, y, w, h)

	def get_distance(self, x, y, w, h):
		pass

	def print(self):
		print('x:{0} y:{1} w:{2} h:{3}'.format(self.x, self.y, self.w, self.h))

def get_egg_info(filepath):
	f = open(filepath, 'r')
	row = csv.reader(f, delimiter=',')

	eggs = [Egg(r[1], r[2], r[3], r[4]) for r in row]
	f.close()

	return eggs
