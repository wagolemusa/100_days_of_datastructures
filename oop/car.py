class Car:
	def __init__(self, speed, color):
		self.speed = speed
		self.color = color


ford = Car(300, 'red')
honda = Car(400,  'blue')
audi = Car(200, 'black')

print(ford.speed)
print(ford.color)