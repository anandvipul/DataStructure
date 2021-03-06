# Doubly Linked List

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class doubly_linked_list:

	def __init__(self):
		self.head = None

# Adding data elements

	def push(self, NewVal):
		NewNode = Node(NewVal)
		NewNode.next = self.head # marks the end of list
		if self.head is not None:
			self.head.prev = NewNode
		self.head = NewNode

# Print the Doubly Linked List

	def listprint(self, node):
		while (node is not None):
			print(node.data)
			last = node
			node = node.next

dllist = doubly_linked_list()
dllist.push(12)
dllist.push(8)
dllist.push(62)
dllist.listprint(dllist.head)
