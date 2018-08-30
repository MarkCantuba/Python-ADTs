class Node(object):
    def __init__(self, value, next_node=None):
        self._value = value
        self._next = next_node

    def set_next(self, value):
        self._next = value

    def has_next(self):
        return self._next is not None

    def get_value(self):
        return self._value

    def next(self):
        return self._next

    def __str__(self):
        return str(self._value) + ";" + str(self._next)