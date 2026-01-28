class Graph:
    def __init__(self):
        self.adjacency_list = {} # Initialize an empty adjacency list to represent the graph by using a dictionary

        
    def add_vertex(self, vertex): # Add a vertex to the graph
        if vertex not in self.adjacency_list: # If the vertex is not already in the adjacency list
            self.adjacency_list[vertex] = []
            
    def add_edge(self, src, dest):
# Add an edge between src and dest
        self.add_vertex(src) 
        self.add_vertex(dest)
        # Add an edge between src and dest
        self.adjacency_list[src].append(dest)
        self.adjacency_list[dest].append(src)  # For undirected graph

    def bfs(self, src):
        visited = set() # Set to keep track of visited nodes
        queue = [src]
        visited.add(src)

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=' ')
            # Explore neighbors
            for neighbor in self.adjacency_list.get(vertex, []):
                # If neighbor has not been visited
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
    
    def print_graph(self):
        for key in self.adjacency_list:
            print(f"{key}: {self.adjacency_list[key]}")
            
# Example usage:
g = Graph()
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_edge(1,4)
g.add_edge(2,5)
g.add_edge(2,6)
g.add_edge(3,7)
g.add_edge(4,5)
g.add_edge(4,6)
g.add_edge(6,2)
g.add_edge(6,7)
g.print_graph()
print("BFS Traversal starting from vertex 0:")
g.bfs(0)

print("\n")
graph=Graph()

graph.add_edge(0,1)
graph.add_edge(0,3)
graph.add_edge(1,3)
graph.add_edge(3,4)
graph.add_edge(3,5)
graph.add_edge(4,5)
graph.add_edge(4,6)
graph.add_edge(6,2)
graph.add_edge(6,7)

graph.print_graph()
print("BFS Traversal starting from vertex 0:")
graph.bfs(0)