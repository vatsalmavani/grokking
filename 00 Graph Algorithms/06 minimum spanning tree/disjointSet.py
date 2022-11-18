# https://www.youtube.com/watch?v=WQbbFhPGBN0

# disjoint set is also known as union find

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

        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[yroot] < self.rank[xroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot    # we could've done vise versa
            self.rank[xroot] += 1
    # O(1) time complexity

vertices = ['a','b','c','d','e']
ds = disjointSet(vertices)

print(ds.findParent("b"))
ds.union('a','b')
print(ds.findParent('b'))
ds.union('a','c')
print(ds.findParent('c'))