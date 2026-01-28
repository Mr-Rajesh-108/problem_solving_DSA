from collections import deque


class Graph:
    def __init__(self,vertices):
        self.mat=[[0]*vertices for _ in range(vertices)]
        self.size=vertices
    def add_edge(self, src,dest):
        # if src>=self.size or dest>=self.size: # Check if the nodes are within bounds
        if 0 <=src<self.size and 0<=dest<self.size: # Check if the nodes are within bounds
            self.mat[src][dest]=1
            self.mat[dest][src]=1
        else:
            raise IndexError("Node index out of bounds")
    
    def bfs(self,src):
        visited=[False]*self.size
        queue=deque([src])
        visited[src]=True
        while queue:
            vertex=queue.popleft()
            print(vertex,end=" -> ")
            for i in range(self.size):
                if self.mat[vertex][i]==1 and  visited[i] == False:
                    visited[i]=True
                    queue.append(i)
        
    def print_graph(self):
        for row in self.mat:
            print(" ".join(map(str,row)))
    
g=Graph(8)
g.add_edge(0,1)
g.add_edge(0,3)
g.add_edge(1,3)
g.add_edge(3,4)
g.add_edge(3,5)
g.add_edge(4,5)
g.add_edge(4,6)
g.add_edge(6,2)
g.add_edge(6,7)
g.print_graph()
print("BFS Traversal starting from vertex 0:")
g.bfs(0)