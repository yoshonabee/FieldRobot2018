class Queue():
	def __init__(self, num=None):
		self.queue = []
		self.num = num

	def size(self):
		return len(self.queue)

	def isEmpty(self):
		return len(self.queue) == 0

	def add(self, item):
		self.queue.append(item)
		if self.num is not None and self.size() > self.num:
			return self.queue.pop(0)
		return None

	def pop(self):
		return self.queue.pop(0)

	def print(self):
		print(self.queue)

	def clear(self):
		while len(self.queue) > 0:
			print(self.queue.pop(0))

	def allNone(self):
		for i in self.queue:
			if i != None:
				return False
		return True

	def get(self):
		for i in self.queue:
			if i != None:
				return i
		return None