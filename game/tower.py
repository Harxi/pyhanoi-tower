import random

class Towers:
	def __init__(self):
		self.towers = [[],[],[]]
	
	def generate(self):
		notExist = [x for x in range(1, 16)]
		for _ in range(0, len(notExist)):
			tile = random.choice(notExist)
			del notExist[notExist.index(tile)]
			self.towers[random.randint(0, 2)].append(tile)
			
	def move(self, fromT, toT):
		self.towers[toT].insert(0, self.towers[fromT][0])
		del self.towers[fromT][0]
	
	def search(self, value):
		for tower in range(0, 3):
			if value in self.towers[tower]:
				return {"tower": tower, "index": self.towers[tower].index(value)}
