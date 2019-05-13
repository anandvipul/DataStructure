# Push into a Stack
'''
In a stack the element insreted last in sequence will come out first 
as we can remove only from the top of the stack. Such feature is 
known as Last in First Out(LIFO) feature. 
The operations of adding and removing the elements is known as 
PUSH and POP. In the following program we implement it as add and 
and remove functions. 
We declare an empty list and use the append() and pop() methods 
to add and remove the data elements.
'''

class Stack:
	def __init__(self):
		self.stack = []
# Use list append method to add element
	def add(self, dataval):
		if dataval not in self.stack:
			self.stack.append(dataval)
			return True
		else:
			return False

# Use peek to look at the top of the stack
	def peek(self):
		return self.stack[-1]
# Use emove to remove element form the stack
	def remove(self):
		if len(self.stack) <= 0:
			return 'There is no element in the stack'
		else:
			return self.stack.pop()
# Use display to see the stack
	def display(self):
		return self.stack


AStack = Stack()
AStack.add('Mon')
AStack.add('Tue')
print(AStack.peek())
AStack.add('Wed')
AStack.add('Thu')

print('\n Display Stack before poping')
print(AStack.display())

print(AStack.remove())
print('\n Displaying the Stack after poping \n')
print(AStack.display())

