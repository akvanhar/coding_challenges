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
            count += 1
            current = current.next
        return count

    def search(self, item):
        # travel through the Linked List and return true
        # if the item is found.
        # return false if we reach the end of the list,
        # and the item is not found

        current = self.head
        while current:
            if current.data == item:
                return True
            else:
                current = current.next
        else:
            return False

    def remove(self, item):
        # remove the first node found with node.data == item

        current = self.head
        previous = None
        found = False
        while not found:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next

        if previous is None:
            self.head = current.next
        else:
            previous.set_next(current.next)

    def append(self, item):
        # add a new node, but instead of putting
        # it at the beginning of the list,
        # travel to the end and append the node there.

        current = self.head
        temp = Node(item)
        while current.next:
            current = current.next
        current.next = temp

    def insert(self, index, item):
        # insert a new node a specific index

        temp = Node(item)
        count = 0
        previous = None
        current = self.head
        if index == 0:
            temp.next = current
            self.head = temp
            return
        elif index == self.size():
            self.append(item)
            return
        else:
            while current:
                if count == index:
                    previous.next = temp
                    temp.next = current
                    return
                else:
                    previous = current
                    current = current.next
                    count += 1
        if count < index:
            print "Sorry, this linked_list is too short for that index"

    def index(self, item):
        # return the index of the particular item
        count = 0
        current = self.head

        while current:
            if current.data == item:
                return count
            else:
                current = current.next
                count += 1
        else:
            print "Sorry. That item wasn't found."

    def pop(self):
        # return the last item in the list, and remove it.
        current = self.head
        previous = None
        if self.head is None:
            print "Sorry. This list is empty."
            return
        while current.next:
            previous = current
            current = current.next
        if previous is None:
            self.head = None
            print current.data
            return current
        else:
            previous.next = None
            print current.data
            return current


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
