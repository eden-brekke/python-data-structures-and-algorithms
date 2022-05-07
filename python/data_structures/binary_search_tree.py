from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    def add(self, value):

        def walk(root, new_node):
            if not root:
                return
            if new_node.value < root.value:
                # go left
                if root.left:
                    walk(root.left, new_node)
                else:
                    root.left = new_node
            else:
                # go right
                if root.right:
                    walk(root.right, new_node)
                else:
                    root.right = new_node

        # we have (5) to add with an overall tree root of (10) because 5 is lessthan 10 then its gotta go left

        node_to_add = Node(value)

        if not self.root:
            self.root = node_to_add
            return

        walk(self.root, node_to_add)

    def contains(self, value):
        if self.root is None:
            return False

        def walk(root, value):
            if root.value == value:
                return True
            elif value > root.value:
                if root.right:
                    return walk(root.right, value)
            elif value < root.value:
                if root.left:
                    return walk(root.left, value)
            return False
        return walk(self.root, value)
