from BLLNode import BiNode
from LinkedList import LinkedList


class BiLinkedList(LinkedList):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return super().__str__()

    def insert_front(self, value):
        if self.is_empty():
            self._root = BiNode(value)
            self._last = self._root
        else:
            new_node = BiNode(value, next_node=self._root)
            self._root.set_prev(new_node)
            self._root = BiNode(value, self._root)
        self._count += 1

    def delete_front(self):
        super().delete_front()
        self._root.set_prev(None)

    def insert_last(self, value):
        if self.is_empty():
            self.insert_front(value)
        else:
            new_node = BiNode(value, prev_node=self._last)
            self._last.set_next(new_node)
            self._last = new_node
        self._count += 1

    def delete_last(self):
        return super().delete_last()

    def insert_at_index(self, index, value):
        return super().insert_at_index(index, value)

    def delete_at_index(self, index):
        return super().delete_at_index(index)

    def contains(self, value):
        return super().contains(value)

    def is_empty(self):
        return super().is_empty()

    def get_root(self):
        return super().get_root()

    def get_last(self):
        return super().get_last()

    def get_at_index(self, index):
        return super().get_at_index(index)

    def length(self):
        return super().length()

    def has_next(self):
        return super().has_next()

    def next(self):
        return super().next()


if __name__ == "__main__":
    print("***** Testing Linked List ADT *****")
    print("\n >>> Creating New Linked List <<<")
    ll = BiLinkedList()
    if not ll.is_empty():
        print("The list should be empty!")
    print("Current State: " + str(ll))

    for i in range(10):
        ll.insert_front(9-i)
    print("Current State after insertion to front: " + str(ll))
    current_index = 0

    for i in range(10):
        if ll.get_at_index(i) != ll.get_at_index(current_index):
            print("The expected value at index " + str(current_index) + " should be " + str(9 - i))
        current_index += 1
    if ll.length() != 10:
        print("Current length should be 10!")

    dup = ll
    while dup.has_next():
        if dup.prev() is not None:
            print(dup.prev().value())
        dup = dup.next()

    print(ll)
    ll.delete_at_index(8)
    ll.delete_at_index(8)
    ll.delete_at_index(4)
    print(ll)







