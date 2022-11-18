class Graph:
    def __init__(self, gdict=None):  # gdict = graph dictionary
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

customDict = {"a": ["b", "c"],
              "b": ["a", "d", "e"],
              "c": ["a", "e"],
              "d": ["b", "e", "f"],
              "e": ["d", "f"],
              "f": ["d", "e"]}

graph = Graph(customDict)
graph.addEdge("c", "d")
print(graph.gdict["c"])

# --------------------------------------------------------------------------



# graph basic methods:
# --------------------------------------------------------------------------

class Graph2:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False
    
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].remove(vertex2)
            self.adjacency_list[vertex2].remove(vertex1)
            return True
        return False

    # Use Python del to Remove a Key from a Dictionary
    # a_dict = {'John': 32, 'Mel': 31, 'Nik': 33, 'Katie': 32, 'James': 29, 'Matt': 35}
    # del a_dict['John']
    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False
    
        

custom_graph = Graph2()
custom_graph.add_vertex("A")
custom_graph.print_graph()

custom_graph.add_vertex("B")
custom_graph.add_edge("A", "B")
custom_graph.print_graph()

print("before removing edge")
custom_graph.add_vertex("C")
custom_graph.add_edge("A", "C")
custom_graph.add_edge("B", "C")
custom_graph.print_graph()
print("after removing edge")
custom_graph.remove_edge("A", "C")
custom_graph.print_graph()

print("before removing vertex")
my_graph = Graph2()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
my_graph.add_edge("A", "B")
my_graph.add_edge("A", "C")
my_graph.add_edge("A", "D")
my_graph.add_edge("B", "C")
my_graph.add_edge("C", "D")
my_graph.print_graph()
print("after removing vertex")
my_graph.remove_vertex("D")
my_graph.print_graph()