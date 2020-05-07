class Rectangle():
	def __init__(self, height, width):
		self.height = height
		self.width = width


ract1 = Rectangle(40, 50)
ract2 = Rectangle(30, 50)

print(ract1.height * ract1.width)
print(ract2.height * ract2.width)