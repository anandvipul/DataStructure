# Adding a new node in the last of the Linked List.


class Node:
	def __init__(self, dataval = None):
		self.dataval = dataval
		self.nextval = None
class SLinkedList:
	def __init__(self):
		self.headval = None

# Print LinkedList
	def listprint(self):
		printval = self.headval
		while printval is not None:
			print(printval.dataval)
			printval = printval.nextval

	def AtEnd(self, newdata):
		NewNode = Node(newdata)
		if self.headval is None:
			self.headval = NewNode
			return
		laste = self.headval
# laste value is updated till it reaches the end
		while(laste.nextval):
			laste = laste.nextval
		laste.nextval = NewNode



list1 = SLinkedList()
list1.headval = Node('Mon')

e2 = Node('Tue')
e3 = Node('Wed')

#Link first Node to Second Node
list1.headval.nextval = e2


#Link Second Node to third Node
e2.nextval = e3



list1.AtEnd('Thu')
list1.listprint()
