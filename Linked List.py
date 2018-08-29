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

    def __init__(self, node):
        self.root = node
        self.count = 1

    def __len__(self):
        return self.count

    def __str__(self):
        if self.is_empty():
            return "Linked List is empty!"
        return self.root.__str__()

    def insert_front(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.root = new_node
        else:
            new_node.set_next(self.root)
            self.root = new_node
        self.count += 1

    def is_empty(self):
        return self.count == 0

    def get_root(self):
        return self.root


ll = LinkedList(Node(1))
ll.insert_front(Node(2))

print(ll)



