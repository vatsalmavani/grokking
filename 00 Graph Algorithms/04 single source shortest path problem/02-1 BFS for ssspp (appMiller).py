# theory: https://www.udemy.com/course/data-structures-and-algorithms-bootcamp-in-python/learn/lecture/22091976#overview
# appMiller's solutionn (hard). See 02-3 file for easy implementation

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict={}
        self.gdict = gdict
    
    # method to find shortest path b/w start vertex and end vertex using bfs
    def bfs(self, start, end):
        # creating queue to maintain path
        queue = []
        queue.append([start])
        while queue: # while queuee is not an empty queue []
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjacent in self.gdict.get(node, []):
                new_path = list(path)   # path is already a list then why list(path)? bcoz list(path) creates a new list. So, although values of the lists are same, if you do print(path is new_path), it will return False as they are not the same objects
                new_path.append(adjacent)
                queue.append(new_path)


customDict = {  "a": ["b", "c"],
                "b": ["d", "g"],
                "c": ["d", "e"],
                "d": ["f"],
                "e": ["f"],
                "g": ["f"]
}

g = Graph(customDict)
print(g.bfs("a", "f"))

# time complexity of bfs method here is O(E) and not O(E + V)
# bcoz we are only visiting the connected vertices and not the isolated ones
# space complexity is also O(E)