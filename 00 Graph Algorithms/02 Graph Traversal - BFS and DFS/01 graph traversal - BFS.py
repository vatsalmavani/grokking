# theory: https://www.udemy.com/course/data-structures-and-algorithms-bootcamp-in-python/learn/lecture/21975868#overview


class Graph:
    def __init__(self, gdict=None):  # gdict = graph dictionary
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
    
    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:    # while queue is not empty
            deVertex = queue.pop(0) # dequeue vertex    # pop(0) means remove from the beginning - same as queue
            print(deVertex, end=" ")
            for adjVertex in self.gdict[deVertex]:  # adjVertex = adjacent vertex
                if adjVertex not in visited:
                    visited.append(adjVertex)
                    queue.append(adjVertex)
    # time complexity is O(V + E) where V = no of vertex & E = no of edges
    # space complexity is also O(V + E) since we are adding stuff in the queue

customDict = {"a": ["b", "c"],
              "b": ["a", "d", "e"],
              "c": ["a", "e"],
              "d": ["b", "e", "f"],
              "e": ["d", "f"],
              "f": ["d", "e"]}

graph = Graph(customDict)
graph.bfs("a")

# when to use?
# if we know that the target is close to the starting point