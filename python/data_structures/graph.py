from data_structures.queue import Queue

class Graph:
    """
    Create a graph of Vertices
    """
    def __init__(self):
        self._adjacency_list = {} # Hashtable leading _ means this is for internal use only.


    def add_node(self, value):
        '''
        Arguments: value
        Returns: The added node
        Add a node to the graph
        '''
        vertex = Vertex(value) # set vertext to the class vertex with the value passed in (node)
        self._adjacency_list[vertex] = [] # set the adjacency list dictionary at index vertex to an empty list (so the node is a list)
        return vertex # return the vertex (node) that has the value in it.

    def add_edge(self, start, end, weight=0):
        '''
        Arguments: 2 nodes to be connected by the edge, weight (optional)
        Returns: nothing
        Adds a new edge between two nodes in the graph
        If specified, assign a weight to the edge
        Both nodes should already be in the Graph
        '''
        if start not in self._adjacency_list or end not in self._adjacency_list: # if there isn't a value at start or end vertices then raise an error
            raise KeyError()
        edge = Edge(end, weight) # set the edge to the class edge which you pass the end point and the weight of the connection to it
        self._adjacency_list[start].append(edge) # append the edge the list that is at the vertex with the start value node

    def get_nodes(self):
        '''
        Arguments: none
        Returns all of the nodes in the graph as a collection (set, list, or similar)
        '''
        return list(self._adjacency_list.keys()) # returns the keys within the dictionary that is adjacency list


    def get_neighbors(self, vertex):
        '''
        Arguments: node
        Returns a collection of edges connected to the given node
        Include the weight of the connection in the returned collection
        '''
        return self._adjacency_list[vertex] # returns the edges connected to the given node

    def size(self):
        '''
        Arguments: none
        Returns the total number of nodes in the graph
        '''
        return len(self._adjacency_list) # return the length of the dictionary



    def breadth_first(self, vertex):
        all_vertices = []
        breadth = Queue()
        visited_vertices = set()
        breadth.enqueue(vertex)
        visited_vertices.add(vertex)

        while not breadth.is_empty():
            front = breadth.dequeue()
            all_vertices.append(front.value)

            for neighbor in self.get_neighbors(front):
                if neighbor.vertex not in visited_vertices:
                    visited_vertices.add(neighbor.vertex)
                    breadth.enqueue(neighbor.vertex)
        return all_vertices

class Vertex:
    '''
    Vertex = Node, holds the value
    '''
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
