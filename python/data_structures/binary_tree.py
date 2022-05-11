from data_structures.queue import Queue

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root=None, values=None):
        self.root = root
        if values:
            for value in values:
                self.add(value)

    def find_maximum_value(self):
        if self.root is None:
            return None

        def walk(root, max):
            if root is None:
                return max
            if root.value > max:
                max = root.value
            max = walk(root.left, max)
            max = walk(root.right, max)
            return max

        result = walk(self.root, 0)
        return result

    def pre_order(self):
        def walk(root, values):
            if not root:
                return
            values.append(root.value)
            walk(root.left, values)
            walk(root.right, values)
        ordered_values = []
        walk(self.root, ordered_values)
        return ordered_values

    def in_order(self):
        # method body here
        def walk(root, values):
            if not root:
                return
            walk(root.left, values)
            values.append(root.value)
            walk(root.right, values)
        ordered_values = []
        walk(self.root, ordered_values)
        return ordered_values

    def post_order(self):
        def walk(root, values):
            if not root:
                return
            walk(root.left, values)
            walk(root.right, values)
            values.append(root.value)
        ordered_values = []
        walk(self.root, ordered_values)
        return ordered_values

    def add(self, value):

        node = Node(value)

        if not self.root:
            self.root = node
            return

        breadth = Queue()

        breadth.enqueue(self.root)

        while not breadth.is_empty():
            front = breadth.dequeue()
            if not front.left:
                front.left = node
                return
            else:
                breadth.enqueue(front.left)

            if not front.right:
                front.right = node
                return
            else:
                breadth.enqueue(front.right)
