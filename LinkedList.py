class Node:
    def __init__(self, data = None, nxt = None):
        self.data = data
        self.nxt = nxt

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.nxt:
                current = current.nxt
            current.nxt = new_node
        else:
            self.head = new_node

    def printLL(self):
        current = self.head
        while (current):
            print(current.data)
            current = current.next

insta = Node(3)
print(insta.data, insta.nxt)

