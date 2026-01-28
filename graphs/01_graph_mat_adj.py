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
           
           

g = Graph(5)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(2,3)

g.print()
