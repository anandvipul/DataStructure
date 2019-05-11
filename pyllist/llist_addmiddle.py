# Adding a new node in the middle of the Linked List.
# In this case we are adding new node after the middle node.

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

	def Inbetween(self, middle_node, newdata):
		if middle_node is None:
			print('The mentioned node is absent')
			return

		NewNode = Node(newdata)
		NewNode.nextval = middle_node.nextval
		middle_node.nextval = NewNode



list1 = SLinkedList()
list1.headval = Node('Mon')

e2 = Node('Tue')
e3 = Node('Thu')

#Link first Node to Second Node
list1.headval.nextval = e2


#Link Second Node to third Node
e2.nextval = e3



list1.Inbetween(list1.headval.nextval,'Fri')
list1.listprint()
