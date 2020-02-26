class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def adding(self, data):
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
        elems.append(current.data)
        while current.next:
            current = current.next
            elems.append(current.data)
        return elems

    def show_any(self, index):
        if index >= self.length():
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

    def del_head(self):
        new_node = self.head
        self.head = self.head.next
        return new_node.data

    def del_end(self):
        current = self.head
        while current.next:
            current = current.next
        last_node = current
        last_node.next = self.head


insta = SinglyLinkedList()
n = Node()
insta.adding(4)
insta.adding(3)
insta.adding(3)
insta.adding(5)
#insta.show_any(1)
n.__repr__()
#insta.del_end()
print(insta.display())


