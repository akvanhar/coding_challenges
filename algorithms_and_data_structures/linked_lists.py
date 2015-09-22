class Linked_List(object):
	# a general representation of a linked list
	# after you initialize the list, set the head pointer

	def __init__(self):
		self.head = None

	def is_empty(self):
		"""
		check to see if the linked_list contains any nodes
			>>> print mylist.is_empty()
			True
		"""

		if self.head:
			return False
		else:
			return True

	def add(self, node_data):
		# add a node to the list. 
		# the new node is the nead of the list
		# other items get pushed further down the list, away from the head
		# first, create a new node with the passed-in data
		# then point the node's next to the current head.
		# point head of the linked list to the new node.
		# return nothing

		temp = Node(node_data)
		temp.set_next(self.head)
		self.head = temp

	def size(self):
		# count the number of objects in the Linked List

		current = self.head
		count = 0
		while current:
			count +=1
			current = current.next
		return count

	def search(self, item):
		# travel through the Linked List and return true
		# if the item is found.
		# return false if we reach the end of the list,
		# and the item is not found


class Node(object):
	# creates an instance of a node for a linked list
	# each node object must have 2 pieces of information
	# the data, and the pointer to the next instance

	def __init__(self, data):
		self.data = data
		self.next = None

	def get_data(self):
		# returns the data of the current node

		return self.data

	def get_next(self):
		# returns the next node in the list

		return self.next

	def set_data(self, new_data):
		# set new data for the current node

		self.data = new_data

	def set_next(self, new_next):
		# set a new pointer to the next node

		self.next = new_next