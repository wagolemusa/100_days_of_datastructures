"""
Stack data structure

"""

class Stack():
	def __init__(self):
		self.items = []

	# push the item in the stock.
	def push(self, item):
		self.items.append(item)

	# remove the last number  in stick
	def pop(self):
		return self.items.pop()

	# check if the item in the stock is empty
	def is_empty(self):
		return self.items == []

	# Pick last item in the item
	def peek(self):
		if not self.is_empty():
			return self.items[-1]

	# print all items in the stock
	def get_stack(self):
		return self.items

s = Stack()
# print(s.is_empty())
# s.push("A")
# print(s.is_empty())
s.push("A")
s.push("B")
print(s.get_stack())
s.push("C")
print(s.get_stack())
s.pop()
print(s.get_stack())
