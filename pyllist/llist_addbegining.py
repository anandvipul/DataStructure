# Adding a new node in the begining of the Linked List.


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

	def AtBegining(self, newdata):
		NewNode = Node(newdata)
# Update the new nodes next val to existing node

		NewNode.nextval = self.headval
		self.headval = NewNode



list1 = SLinkedList()
list1.headval = Node('Mon')

e2 = Node('Tue')
e3 = Node('Wed')

#Link first Node to Second Node
list1.headval.nextval = e2


#Link Second Node to third Node
e2.nextval = e3



list1.AtBegining('Sun')
list1.listprint()
