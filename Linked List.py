from LLNode import Node

class LinkedList(object):

    def __init__(self):
        self._root = None
        self._last = None
        self._count = 0

    def __len__(self):
        return self._count

    def __str__(self):
        if self.is_empty():
            return "Linked List is empty!"
        return self._root.__str__()

    def insert_front(self, value):
        if self.is_empty():
            self._root = Node(value)
            self._last = self._root
        else:
            self._root = Node(value, self._root)
        self._count += 1

    def insert_last(self, value):
        if self.is_empty():
            self.insert_front(value)
        else:
            new_node = Node(value)
            self._last.set_next(new_node)
            self._last = new_node
        self._count += 1

    def insert_at_index(self, index, value):
        if self._count <= index:
            raise Exception("Index cannot be greater than the size of our list!s")
        if self.is_empty() or index == 0:
            self.insert_front(value)
        elif self.length() - 1 == index:
            self.insert_last(value)
        else:
            curr = self._root
            prev = None
            counter = 0
            while counter != index:
                prev = curr
                curr = curr.next()
                counter += 1
            prev.set_next(Node(value))
            prev.next().set_next(curr)
        self._count += 1

    def contains(self, value):
        curr = self._root
        while curr.get_value() != value and curr.has_next():
            curr = curr.next()
            if curr.get_value() == value:
                return True
        return False

    def is_empty(self):
        return self._count == 0

    def get_root(self):
        return self._root

    def get_last(self):
        return self._last

    def get_at_index(self, index):
        current = self._root
        counter = 0
        while counter != index:
            current = current.next()
            counter += 1
        return current.get_value()

    def length(self):
        return self._count


if __name__ == "__main__":
    print("***** Testing Linked List ADT *****")


