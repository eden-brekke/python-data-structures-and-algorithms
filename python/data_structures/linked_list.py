class LinkedList:
    """
    This class is used to create a Linked List that will initialize with an Empty head
    It will also allow for new Nodes to be added with their own values, moving the old head-node to the next node
    """

    def __init__(self):
        # initialization here, instance attributes get defined in here
        self.head = None  # Initialize the Linked List with a Head Node with the Value of None

    def insert(self, value):
        # Create a new Node calling the Node class
        self.head = Node(value, self.head)

    def __str__(self):
        # Take in a response and return a string of the current nodes while traversing
        response = ""
        current = self.head  # Start at the head and work your way through the Linked List
        while current:
            response += f"{{ {str(current.value)} }} -> "
            current = current.next
        return response + "NULL"

    def includes(self, value):
        # Use this method to check if a value is currently within the Linked List
        current = self.head  # Start at the head and work your way through the Linked List

        # Use this while loop to step through each of the nodes within the link list
        # While stepping through the linked list check if the value is present and return True if so.
        # If not present while loop while break and return False
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def append(self, value):
        new_node = Node(value)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
        return new_node

    def insert_before(self, value, new_value):
        previous = current = self.head
        if self.head is None:
            raise TargetError
        if self.includes(value) is False:
            raise TargetError

        while current:
            if value == current.value:
                new_node = Node(new_value)
                if current == self.head:
                    new_node.next = self.head
                    self.head = new_node
                    return new_node
                else:
                    previous.next = new_node
                    new_node.next = current
                    return new_node
            else:
                previous = current
                current = current.next

    def insert_after(self, value, new_value):
        current = self.head
        if self.head is None:
            raise TargetError
        if self.includes(value) is False:
            raise TargetError
        while current:
            if current.value == value:
                new_node = Node(new_value)
                new_node.next = current.next
                current.next = new_node
                return new_node
            else:
                current = current.next

    def find_length_of_linked_list(self):
        """
        This is a helper method that will count all the nodes within a list as it traverses
        Then it will return the count
        """
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next
        return count

    def kth_from_end(self, k):
        """
        This method will take in a number as an argument (k)
        Then the method will return the node's value that is the k'th index from the end of the list
        """
        if k >= 0:
            current = self.head
            length = self.find_length_of_linked_list()
            target = length - k

            if target < 1:
                raise TargetError
            for i in range(1, target):
                current = current.next
            return current.value
        else:
            raise TargetError



class Node:
    """
    Class to create a New Node
    """

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class TargetError(Exception):
    pass
