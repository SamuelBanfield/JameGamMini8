class Player:
	def __init__(self, x, y, scene = None):
		self.x, self.y = x, y
		self.speed = 5
		self.scene = scene
