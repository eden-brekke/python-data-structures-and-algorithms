from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError


class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.front = None
        self.rear = None

    def enqueue(self, value):
        # method body here
        if self.rear:
            self.rear.next = Node(value)
            self.rear = self.rear.next
        else:
            self.rear = Node(value)
            self.front = self.rear

    def dequeue(self):
        if self.front is None:
            raise InvalidOperationError
        temporary_value = self.front
        self.front = self.front.next
        temporary_value.next = None
        return temporary_value.value

    def peek(self):
        if not self.front:
            raise InvalidOperationError
        else:
            return self.front.value

    def is_empty(self):
        if self.front is None:
            return True
        return False
