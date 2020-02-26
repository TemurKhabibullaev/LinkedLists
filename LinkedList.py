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

    def length(self):
        current = self.head
        total = 1
        while current.next:
            total += 1
            current = current.next
        print(total)

    def display(self):
        elems = []
        current = self.head
        elems.append(current.data)
        while current.next:
            current = current.next
            elems.append(current.data)
        print(elems)

    def show_any(self, index):
        list = []
        current = self.head
        list.append(current)
        while current.next:
            current = current.next
            list.append(current)
        if index > len(list):
            print("ERROR. Out of range")
        print(list[index])

    def erase_any(self, index):
        list = []
        current = self.head
        list.append(current)
        while current.next:
            current = current.next
            list.append(current)
        if index > len(list):
            print("ERROR. Out of range")
        del list[index]
        print(list)

    def del_head(self):
        self.head = self.head.next

    def del_end(self):
        list = []
        current = self.head
        list.append(current)
        while current.next:
            current = current.next
            list.append(current)
        del list[-1]
        print(list)

    def rem_obj(self, object):
        list = []
        current = self.head
        list.append(current.data)
        while current.next:
            current = current.next
            list.append(current.data)
        if int(object) == current.data: list.remove(current.data)
        elif int(object) != current.data: print("Error. No such value")
        print(list)

    def container(self, object):
        list = []
        current = self.head
        list.append(current.data)
        while current.next:
            current = current.next
            list.append(current.data)
        if int(object) in list: print(True)
        else: print(False)

insta = SinglyLinkedList()
insta.adding(4)
insta.adding(3)
insta.add_head(2)
#insta.length()
insta.rem_obj(3)
insta.display()


