# Graphs
<!-- Short summary or background information -->
Graphs are a non-linear data structure.

## Challenge
<!-- Description of the challenge -->
Implement Graphs as a new Data Structure

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Graph Big(O) is O(N) where N is the number of vertices added

## API
<!-- Description of each method publicly available in your Graph -->
**add node**

- Arguments: value
- Returns: The added node
- Add a node to the graph

**add edge**

- Arguments: 2 nodes to be connected by the edge, weight (optional)
- Returns: nothing
- Adds a new edge between two nodes in the graph
- If specified, assign a weight to the edge
- Both nodes should already be in the Graph

**get nodes**

- Arguments: none
- Returns all of the nodes in the graph as a collection (set, list, or similar)

**get neighbors**

- Arguments: node
- Returns a collection of edges connected to the given node
- Include the weight of the connection in the returned collection

**size**

- Arguments: none
- Returns the total number of nodes in the graph
