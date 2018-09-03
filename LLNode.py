# @Author: Mark Cantuba


class Node(object):
    def __init__(self, value, next_node=None):
        """
        Constructor method that creates our node object
        :param value: value to be set in our node
        :param next_node: Optional next node!
        """
        self._value = value
        self._next = next_node

    def set_next(self, value):
        """
        Set next node to a given value
        :param value: value to be inserted
        """
        self._next = value

    def has_next(self):
        """
        Check if the current node has a node connected.
        :return: true if it has a next value
        """
        return self._next is not None

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

    def __str__(self):
        return str(self._value) + ";" + str(self._next)
