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

    def dfs_util(self, vertex, visited): # utility function for DFS
        visited.add(vertex) # mark the current vertex as visited
        print(vertex, end=' ') # process the current vertex

        for neighbor in self.adjList[vertex]: # recur for all the vertices adjacent to this vertex
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, start_vertex): # function to perform DFS traversal
        visited = set() # set to keep track of visited vertices
        self.dfs_util(start_vertex, visited) # call the utility function    
    
    def printGraph(self): # function to print the graph
        for vertex in self.adjList:
            print(vertex," -> ",self.adjList[vertex], end="\n")
    
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
print("Depth-First Search starting from vertex 1:")
g.dfs(1)
