class Robot:
	""" A fantastic robot class """
	number_of_Robot = 0
	def __init__(self, name, color, weight):
		self.name = name
		self.color = color
		self.weight = weight
		self.number_of_Robot += 1
		
	def introduce(self):
		""" A method that introduces the robot"""
		print(f"I am a robot. My name is {self.name}. I am {self.weight} kg. I am {self.color} in color. ")
		
		
robo_1 = Robot("Astro", "Gray", 32)

print(robo_1.introduce())
		
		
		