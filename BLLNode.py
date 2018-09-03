from LLNode import Node


class BiNode(Node):

    def __init__(self, value, next_node=None, prev_node=None):
        super().__init__(value, next_node)
        self._prev = prev_node

    def set_next(self, value):
        super().set_next(value)

    def set_prev(self, value):
        self._prev = value

    def has_next(self):
        return super().has_next()

    def has_prev(self):
        return self._prev is not None

    def get_value(self):
        return super().get_value()

    def next(self):
        return super().next()

    def prev(self):
        return self._prev

    def __str__(self):
        return super().__str__()
