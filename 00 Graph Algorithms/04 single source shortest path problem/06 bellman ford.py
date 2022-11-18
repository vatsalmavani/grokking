class Graph:
    def __init__(self, num_of_vertices):
        self.num_of_vertices = num_of_vertices
        self.graph = []
        self.nodes = []

    def add_edge(self, start, destination, weight):
        self.graph.append([start, destination, weight])

    def add_node(self, value):
        self.nodes.append(value)
    
    def print_solution(self, distance: dict):
        print("vertex distsance from the source is:")
        for key, value in distance.items():
            print(str(key) + ": " + str(value))

    def bellmanFord(self, src):
        dist = {i : float('inf') for i in self.nodes} # distance   # -----> O(V)
        dist[src] = 0

        # bellman ford algo should have completed all relaxation in V-1 iterations
        for _ in range(self.num_of_vertices - 1):   # --------------------> O(V)
            for s, d, w in self.graph:  # s: start, d: destination, w: weight   # ---------> O(E)
                if dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w
                
        # if it didn't complete all relaxation in V-1 iters, there is a negative cycle
        for s, d, w in self.graph:      # ------------> O(E)
            if dist[s] + w < dist[d]:
                print("there is a negative cycle in this graph")
                return
        
        self.print_solution(dist)
    # time complexity = O(EV)
    # space complexity = O(V)

g = Graph(5)
g.add_node("a")
g.add_node("b")
g.add_node("c")
g.add_node("d")
g.add_node("e")
g.add_edge("a", "c", 6)
g.add_edge("a", "d", 6)
g.add_edge("b", "a", 3)
g.add_edge("c", "d", 1)
g.add_edge("d", "c", 2)
g.add_edge("d", "b", 1)
g.add_edge("e", "b", 4)
g.add_edge("e", "d", 2)
g.bellmanFord("e")

g2 = Graph(5)
g2.add_node("a")
g2.add_node("b")
g2.add_node("c")
g2.add_node("d")
g2.add_node("e")
g2.add_edge("a", "c", 6)
g2.add_edge("a", "d",-6)     # this creates negative cycle
g2.add_edge("b", "a", 3)
g2.add_edge("c", "d", 1)
g2.add_edge("d", "c", 2)
g2.add_edge("d", "b", 1)
g2.add_edge("e", "b", 4)
g2.add_edge("e", "d", 2)
g2.bellmanFord("e")