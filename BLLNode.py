class BiNode:
    def __init__(self, value, next_node=None):
        """
        Constructor method to create our bi-linked node
        :param value: value to be set to our node
        :param next_node: next node in our bi-linked node
        """
        self._prev = None
        self._value = value
        self._next = next_node

    def __str__(self):
        """
        To String method that will print out a string representation of our node
        """
        return str(self._value) + ";" + str(self._next)

    def set_next(self, value):
        """
        Set next node to a given value
        :param value: value to be inserted
        """
        self._next = value

    def set_prev(self, value):
        """
        Set prev node to a given value
        :param value: value to be inserted
        """
        self._prev = value

    def has_next(self):
        """
        Check if the current node has a node connected.
        :return: true if it has a next value
        """
        return self._next is not None

    def has_prev(self):
        """
        Check if the current node has a node connected to the previous side.
        :return: true if it has a prev value
        """
        return self._prev is not None

    def get_value(self):
        """
        Get value of this node
        :return: return the value this node is holding
        """
        return self._value

    def next(self):
        """
        Get the next item connected to this node
        :return: next value
        """
        return self._next

    def previous(self):
        """
        Get the next item connected to this node
        :return: next value
        """
        return self._prev



