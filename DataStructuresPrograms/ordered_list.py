class Node:     # Node class

    def __init__(self, data):        # Constructor to initialize the node object
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):      # Function to initialize head
        self.head = None

    def sortedInsert(self, new_node):

        if self.head is None:               # Special case for the empty linked list
            new_node.next = self.head
            self.head = new_node

        elif self.head.data >= new_node.data:       # Special case for head at end
            new_node.next = self.head
            self.head = new_node

        else:
            current = self.head     # Locate the node before the point of insertion
            while (current.next is not None and
                   current.next.data < new_node.data):
                current = current.next

            new_node.next = current.next
            current.next = new_node

    def push(self, new_data):           # Function to insert a new node at the beginning
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):        # Utility function to print it the linked LinkedList
        temp = self.head
        while (temp):
            print
            temp.data,
            temp = temp.next


if __name__ == '__main__':

    llist = LinkedList()
    new_node = Node(5)
    llist.sortedInsert(new_node)
    new_node = Node(10)
    llist.sortedInsert(new_node)
    new_node = Node(7)
    llist.sortedInsert(new_node)
    new_node = Node(3)
    llist.sortedInsert(new_node)
    new_node = Node(1)
    llist.sortedInsert(new_node)
    new_node = Node(9)
    llist.sortedInsert(new_node)
    print(llist.printList())

    llist.printList()       # Create Linked List
