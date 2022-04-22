class LinkedList:
    """
    This class is used to create a Linked List that will initialize with an Empty head
    It will also allow for new Nodes to be added with their own values, moving the old head-node to the next node
    """

    def __init__(self):
        # initialization here, instance attributes get defined in here
        self.head = None # Initialize the Linked List with a Head Node with the Value of None

    def insert(self, value):
        # Create a new Node calling the Node class
        self.head = Node(value, self.head)

    def __str__(self):
        # Take in a response and return a string of the current nodes while traversing
        response = ""
        current = self.head # Start at the head and work your way through the Linked List
        while current:
            response += f"{{ {str(current.value)} }} -> "
            current = current.next_node
        return response + "NULL"

    def includes(self, value):
        # Use this method to check if a value is currently within the Linked List
        current = self.head # Start at the head and work your way through the Linked List

        # Use this while loop to step through each of the nodes within the link list
        # While stepping through the linked list check if the value is present and return True if so.
        # If not present while loop while break and return False
        while current:
            if current.value == value:
                return True
            current = current.next_node
        return False


class Node:
    """
    Class to create a New Node
    """
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class TargetError:
    pass
