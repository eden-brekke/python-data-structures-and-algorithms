from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def breadth_first(tree):
    breadth = Queue()
    nodes = []

    if not tree:
        return nodes
    if not tree.root:
        return nodes
