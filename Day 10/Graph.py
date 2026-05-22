# Graph Representation Using Adjacency Matrix
class Graph:
    def __init__(self, vertices):
        # Total number of vertices
        self.V=vertices

        #creates adjacency matrix wwith all 0s
        self.matrix=[[0 for _ in range(vertices)]
                        for _ in range(vertices)]
    
    # Add edge between two vertices 
    def display(self):
        for row in self.matrix:
            print(row)
    
    def add_edge(self, u, v):
        self.matrix[u][v]=1
        self.matrix[v][u]=1

    def remove_edge(self, u, v):
        self.matrix[u][v]=0
        self.matrix[v][u]=0


Obj=Graph(4)
Obj.display()
print()
print("Adjacency Matrix: ")
Obj.add_edge(0,1)
Obj.add_edge(0,2)
Obj.add_edge(1,3)
Obj.add_edge(2,3)
Obj.display()
print()
Obj.remove_edge(0,2)
Obj.display()
