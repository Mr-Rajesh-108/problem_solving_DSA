

class Graph:
    def __init__(self):
        self.adjList = {}
    
    def add_vertex(self,vertex): # function to add vertex
        if vertex not in self.adjList: # if vertex is not present in adjacency list
            self.adjList[vertex] = [] # add vertex with empty list

    def add_edge(self, src, dest): # function to add edge
        self.add_vertex(src) # ensure source vertex is in adjacency list
        self.add_vertex(dest) # ensure destination vertex is in adjacency list

        self.adjList[src].append(dest) # add edge from source to destination
        self.adjList[dest].append(src) # add edge from destination to source (for undirected graph)

    def printGraph(self): # function to print the graph
        for vertex in self.adjList:
            print(vertex," -> ",self.adjList[vertex], end="\n")


# exporting the Graph class for external use


# Example usage:

g = Graph()
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(1, 4)
g.add_edge(4, 3)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(3, 5)

g.printGraph()