class Node(object):
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def set_next(self, value):
        self.next = value

    def has_next(self):
        return self.next is not None

    def get_value(self):
        return self.value

    def next(self):
        return self.next

    def __str__(self):
        return str(self.value) + ";" + str(self.next)


class LinkedList(object):

    def __init__(self):
        self.root = None
        self.count = 0

    def __len__(self):
        return self.count

    def __str__(self):

        if self.is_empty():
            return "Linked List is empty!"
        return self.root.__str__()

    def insert_front(self, value):
        if self.is_empty():
            self.root = Node(value)
        else:
            self.root = Node(value, self.root)
        self.count += 1

    def is_empty(self):
        return self.count == 0

    def get_root(self):
        return self.root


ll = LinkedList()
ll.insert_front(10)
ll.insert_front(11)
ll.insert_front(12)

print(ll.count)



