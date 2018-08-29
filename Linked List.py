class Node(object):
    __value = 0
    _next = None

    def __init__(self, value):
        self.__value = value
        self.__next = None

    def __str__(self):
        return "Value: " + str(self.__value) + " ; Next: " + str(self.__next) + " "


class LinkedList(object):
    __rootNode: Node = None
    __currNode: Node = None

    def __init__(self, root_value):
        self.__rootNode = Node(root_value)

    def is_empty(self):
        return self.__rootNode is None

    def go_root(self):
        self.__currNode = self.__rootNode

    def next(self):
        if self.__currNode._next is not None:
            self.__currNode = self.__currNode._next
        else:
            pass

    def has_next(self):
        return self.__currNode._next is not None

    def get_curr_node(self):
        if self.is_empty():
            return "Linked List is empty!"
        return self.__currNode

    def get_root(self):
        if self.is_empty():
            return "Linked List is empty!"
        return self.__rootNode

    def get_next(self):
        if self.is_empty():
            return "Linked List is empty!"
        return self.__rootNode._next

    def __str__(self):
        string = ""
        if self.is_empty():
            return "Linked list is empty!"
        else:
            self.go_root()
            while self.has_next():
                string += self.__currNode
                self.next()
            return string

