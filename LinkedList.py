class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class SinglyLinkedList:
    def __init__(self):
        self.head = Node()

    def add(self, data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def add_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def length(self):
        current = self.head
        total = 0
        while current.next:
            total += 1
            current = current.next
        return total

    def display(self):
        elems = []
        current = self.head
        while current.next:
            elems.append(current.data)
            current = current.next
        return elems

    def show_any(self, index):
        if index>=self.length():
            print("Out of range")
            return None
        cur_idx = 0
        current = self.head
        while True:
            current = current.next
            if cur_idx == index:
                return current.data
            cur_idx += 1

    def erase_any(self, index):
        if index >= self.length():
            print("Out of range")
            return None
        cur_idx = 0
        current = self.head
        while True:
            current = current.next
            last_node = current
            if cur_idx == index:
                last_node.next = current.next
                return
            cur_idx += 1


insta = SinglyLinkedList()

insta.add_head(4)
insta.add_head(3)
insta.add_end(5)
print(insta.display())


