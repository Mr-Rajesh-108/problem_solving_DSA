class Graph:
    def __init__(self,vertex): # initialize the matrix
        self.size = vertex # number of vertices
        self.mat = [[0]*vertex for _ in range(vertex)] # create a size x size matrix initialized to 0

    def add_edge(self,src, dest): # function to add edge
        if 0 <= src < self.size and 0 <= dest < self.size:  # check for valid vertices
            # graph UNDIRECTED
            self.mat[src][dest] = 1
            self.mat[dest][src] = 1 
        else:
            print("Invalid Edge")
    
    def print(self):
        for row in self.mat:
           print(" ".join(map(str,row))) 
           
    
    def dfs(self, src):
        visited = [False] * self.size  # Track visited vertices
        stack = [src]  # Initialize stack with the source vertex
        while stack:
            vertex = stack.pop()  # Get the last vertex added to the stack
            if visited[vertex] == False:
                print(vertex, end=" -> ")  # Process the vertex (here we just print it)
                visited[vertex] = True  # Mark the vertex as visited
                # Add all unvisited adjacent vertices to the stack
                for i in range(self.size):
                    if self.mat[vertex][i] == 1 and visited[i] == False: # Check for an edge and if not visited
                        stack.append(i)

g = Graph(5)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(2,3)

g.print() # Print adjacency matrix
print("DFS Traversal starting from vertex 0:")
g.dfs(0)  # Start DFS from vertex 0
