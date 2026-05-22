class Graph:
    def __init__(self):
        self.adjancency_list={}

    def add_vertex(self, vertex):
        if vertex not in self.adjancency_list.keys():
            self.adjancency_list[vertex]=[]
            return True
        return False

    def print_graph(self):
        for vertex in self.adjancency_list:
            print(vertex, ":" , self.adjancency_list[vertex])
    
    def add_edges(self, vertex1, vertex2):
            if vertex1 in self.adjancency_list.keys() and vertex2 in self.adjancency_list.keys():
                self.adjancency_list[vertex1].append(vertex2)
                return True
            return False

    def removeVertex(self, vertex):           
        if vertex in self.adjancency_list.keys():
            self.adjancency_list.pop(vertex)
        
obj=Graph()
obj.add_vertex("A")
obj.add_vertex("B")
obj.add_vertex("C")
obj.add_vertex("D")
obj.add_vertex("E")
obj.print_graph()
print()
obj.add_edges("A","B")
obj.add_edges("A","C")
obj.add_edges("A","D")
obj.add_edges("B","A")
obj.add_edges("B","E")
obj.add_edges("C","A")
obj.add_edges("C","D")
obj.add_edges("D","A")
obj.add_edges("D","C")
obj.add_edges("D","E")
obj.add_edges("E","B")
obj.add_edges("E","D")
obj.print_graph()
obj.removeVertex("")
print()
obj.print_graph()

