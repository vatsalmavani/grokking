# do kruskal for this input:
ipt = [[1,2,1], [1,3,3], [2,6,4], [3,4,1], [3,6,2], [4,5,5], [6,7,2], [6,5,6], [7,5,7]]


class disjointSet:
    def __init__(self, vertices):   # make set method
        self.vertices = vertices    # vertices OR nodes are same
        self.parent = {}
        for v in self.vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(self.vertices, 0)
    # O(V) time and space complexity
    
    def findParent(self, vertex):
        if self.parent[vertex] == vertex:   # vertex OR node are same
            return vertex
        else:
            return self.findParent(self.parent[vertex])
    # O(1) time complexity

    def union(self, x, y):  # union of two NODES
        xroot = self.findParent(x)
        yroot = self.findParent(y)
        if xroot != yroot:
            if self.rank[xroot] < self.rank[yroot]:
                self.parent[xroot] = yroot
                self.rank[xroot] += self.rank[yroot]
            else:
                self.parent[yroot] = xroot
                self.rank[yroot] += self.rank[xroot]
    # O(1) time complexity

class Graph:
    def __init__(self, vertices):
        self.v = vertices   # no of vertices
        self.graph = []
        self.nodes = []
        self.MST = []   # minimum spanning tree

    def addEdge(self, s, d, w):     # start, destination, weight
        self.graph.append([s,d,w])
    
    def addNode(self, value):
        self.nodes.append(value)
    
    def printSolution(self):
        for s,d,w in self.MST:
            print(f'{s} - {d}: {w}')

    
    def kruskal(self):
        i, e = 0, 0     # e = no of edges in MST
        ds = disjointSet(self.nodes)
        # how to use lambda function: https://www.w3schools.com/python/python_lambda.asp
        self.graph = sorted(self.graph, key=lambda graph:graph[2])  # graph will be sorted based on weights of the edges
        while e < self.v - 1:   # e is the number of edges in the MST I presume. We increase e if the parents aren't the same because that's when we add a new edge to the tree as we connect two disconnected components.
                                # If x == y that means the two nodes are already in the same connected component so adding an edge would result in a cycle (and not a tree) which is why the condition is x != y.
                                # The loop stops when e == v - 1 because a tree with v vertices contains v - 1 edges.
            s,d,w = self.graph[i]
            i += 1
            x = ds.findParent(s)
            y = ds.findParent(d)
            if x != y:  # if parents of x and y are not same
                e += 1
                self.MST.append([s,d,w])
                ds.union(x, y)
        self.printSolution()



g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addEdge("A", "B", 5)
g.addEdge("A", "C", 13)
g.addEdge("A", "E", 15)
g.addEdge("B", "A", 5)
g.addEdge("B", "C", 10)
g.addEdge("B", "D", 8)
g.addEdge("C", "A", 13)
g.addEdge("C", "B", 10)
g.addEdge("C", "E", 20)
g.addEdge("C", "D", 6)
g.addEdge("D", "B", 8)
g.addEdge("D", "C", 6)
g.addEdge("E", "A", 15)
g.addEdge("E", "C", 20)

g.kruskal()