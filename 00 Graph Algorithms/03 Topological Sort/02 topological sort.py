# topological sort is only on directed acyclic graphs (DAG)
# this is DFS implementation (see this video for widely used dfs implementation - recursion: https://www.youtube.com/watch?v=IG1ABs6lVMw&list=PLdylWCIGC6gebPnAqkoFNbij9bBHbX8__&index=2)

from collections import defaultdict

class Graph:
    def __init__(self, numOfVertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.numOfVertices = numOfVertices

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)


    def topologicalSortUtil(self, vertex, visited: list, stack: list):     # toposort = topological sort
        visited.append(vertex)
        for adjacentVertex in self.graph[vertex]:
            if adjacentVertex not in visited:
                self.topologicalSortUtil(adjacentVertex, visited, stack)
        stack.insert(0, vertex)
    
    def topologicalSort(self):
        visited = []
        stack = []

        for key in list(self.graph):
            if key not in visited:
                self.topologicalSortUtil(key, visited, stack)
        
        print(stack)
    # time and space complexities are O(V + E)


customGraph = Graph(8)
customGraph.addEdge("a", "c")
customGraph.addEdge("c", "e")
customGraph.addEdge("e", "h")
customGraph.addEdge("e", "f")
customGraph.addEdge("f", "g")
customGraph.addEdge("b", "d")
customGraph.addEdge("b", "c")
customGraph.addEdge("d", "f")

customGraph.topologicalSort()