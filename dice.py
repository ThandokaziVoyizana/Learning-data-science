from random import randint

class Die:
	"""Create a simple die class."""
	def __init__(self, sides=6):
		self.sides =sides

	def roll_die(self):
		print(randint(1, self.sides))

die = Die(20)
for _ in range(0, 10):
	die.roll_die()