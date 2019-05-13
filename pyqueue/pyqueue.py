# Queue implementation in python

class Queue:
	def __init__(self):
		self.queue = list()

# Insert, a method to add elements
	def insert(self, dataval):
		if dataval not in self.queue:
			self.queue.insert(0, dataval)
			return True
		else:
			return False
# Display funtion for diplaying the current queue
	def display(self):
		return self.queue

# Remove funtion for removing elements form the queue

	def remove(self):
		if len(self.queue) > 0:
			return self.queue.pop()
		else:
			return ("No Elements in Queue")

q1 = Queue()
q1.insert('Shilpi')
q1.insert('Vipul')

print('The Queue', q1.display())

q1.insert('Shivam')
q1.insert('Mummy')
print('\n The queue \n')
print(q1.display())
print('\n After blowing off \n')
q1.remove()
print(q1.display())
