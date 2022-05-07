class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

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
        # method body here
        def walk(root, values):
            if not root:
                return
            walk(root.left, values)
            walk(root.right, values)
            values.append(root.value)
        ordered_values = []
        walk(self.root, ordered_values)
        return ordered_values
