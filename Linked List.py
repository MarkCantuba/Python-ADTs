# @Author: Mark Cantuba

from LLNode import Node


class LinkedList(object):
    """
    A Linked List ADT
    """
    def __init__(self):
        """
        Constructor method that initializes our Linked List. Creates an empty linked list!
        """
        self._root = None
        self._last = None
        self._count = 0

    def __str__(self):
        """
        To String method to print out a string representation of our linked list
        :return: String representation of our linked list
        """
        if self.is_empty():
            return "Linked List is empty!"
        return self._root.__str__()

    def insert_front(self, value):
        """
        Insert a value in the beginning of our list at index 0
        :param value: value
        """
        if self.is_empty():
            self._root = Node(value)
            self._last = self._root
        else:
            self._root = Node(value, self._root)
        self._count += 1

    def insert_last(self, value):
        """
        Insert a new node at the end of our list
        :param value: Value to be inserted in our linked list
        """
        if self.is_empty():
            self.insert_front(value)
        else:
            new_node = Node(value)
            self._last.set_next(new_node)
            self._last = new_node
        self._count += 1

    def insert_at_index(self, index, value):
        """
        Insert a new value located at index 'index'
        :param index: index position our value to be inserted
        :param value: value to be inserted in pos index
        """
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
        """
        Does our list contain item 'value'
        :param value: value to be searched in our linked list
        :return: True if item exist in our list
        """
        curr = self._root
        while curr.get_value() != value and curr.has_next():
            if curr.get_value() == value:
                return True
            curr = curr.next()
        return False

    def is_empty(self):
        """
        Is our list empty?
        :return: True if our list is empty
        """
        return self._count == 0

    def get_root(self):
        """
        Get the root value in our linked list. None if the list is empty!
        :return: root node
        """
        return self._root

    def get_last(self):
        """
        Get the last item in our linked list
        :return: last item in our list
        """
        return self._last

    def get_at_index(self, index):
        """
        Get the item in index n, first node being at index 0
        :param index: position starting at index 0
        :return: value in index n
        """
        current = self._root
        counter = 0
        while counter != index:
            current = current.next()
            counter += 1
        return current.get_value()

    def length(self):
        """
        Get the current size of our linked list
        :return: node count of our linked list
        """
        return self._count


if __name__ == "__main__":
    print("***** Testing Linked List ADT *****")
    print("\n >>> Creating New Linked List <<<")
    ll = LinkedList()
    if not ll.is_empty():
        print("The list should be empty!")
    print("Current State: " + str(ll))

    for i in range(10):
        ll.insert_front(i)
    print("Current State after insertion to front: " + str(ll))
    current_index = 0

    for i in range(10):
        if ll.get_at_index(i) != ll.get_at_index(current_index):
            print("The expected value at index " + str(current_index) + " should be " + str(9 - i))
        current_index += 1
    if ll.length() != 10:
        print("Current length should be 10!")


