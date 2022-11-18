# theory: https://www.udemy.com/course/data-structures-and-algorithms-bootcamp-in-python/learn/lecture/22013332#overview

class Graph:
    def __init__(self, adjacency_list=None):
        if adjacency_list is None:
            adjacency_list = {}
        self.adjacency_list = adjacency_list
    
    def addEdge(self, vertex, edge):
        self.adjacency_list[vertex].append(edge)

    # AppMiller's approach
    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:    # while stack is not empty
            popVertex = stack.pop()
            print(popVertex, end=" ")
            for adjacentVertex in self.adjacency_list[popVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)
# time and space complexity is O(V + E)
# V = no of vertex & E = no of edges

    # generally used recursive approach
    def DFS(self, source, visited=set()):
        visited.add(source)
        print(source, end=" ")
        for neighbour in self.adjacency_list[source]:
            if neighbour not in visited:
                self.DFS(neighbour, visited)


# note: in bfs, we used queue and in dfs, we're using stack. Not much difference in terms of code

customDict = {"a": ["b", "c"],
              "b": ["a", "d", "e"],
              "c": ["a", "e"],
              "d": ["b", "e", "f"],
              "e": ["d", "f"],
              "f": ["d", "e"]}

graph = Graph(customDict)
graph.dfs("a")
print()
graph.DFS("a")


# when to use?
# if we already know that the target vertex is burried very deep