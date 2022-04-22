class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here, instance attributes get defined in here
        self.head = None

    def insert(self, value):
        # Create a new Node
        self.head = Node(value, self.head)

    def __str__(self):
        response = ""
        current = self.head
        while current:
            response += f"{{ {str(current.value)} }} -> "
            current = current.next
        return response + "NULL"

    def includes(self, value):
        current = self.head

        while current:
            if current.value == value:
                return True
            current = current.next
        return False


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class TargetError:
    pass
