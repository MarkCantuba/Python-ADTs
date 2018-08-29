class Node(object):
    __value = 0
    __next = None

    def __init__(self, value):
        self.__value = value
        self.__next = None

    def __str__(self):
        return "Value: " + str(self.__value) + " ; Next: " + str(self.__next)


class LinkedList(object):
    __rootNode: Node = None

    def __init__(self, value):
        self.__rootNode = Node(value)

print(Node(10))




