from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def breadth_first(tree):
    breadth = Queue()
    nodes = []

    if not tree:
        return nodes
    if not tree.root:
        return nodes
    if not breadth.front:
        breadth.enqueue(tree.root)
    while breadth.front:
        root = breadth.dequeue()
        nodes.append(root.value)
        if root.left:
            breadth.enqueue(root.left)
        if root.right:
            breadth.enqueue(root.right)
    return (nodes)
