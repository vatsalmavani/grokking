# problem: https://leetcode.com/problems/redundant-connection/
# sol: https://leetcode.com/problems/redundant-connection/discuss/989691/Union-Find-(Disjoint-Set)-or-Explanation-%2B-Visual-or-Python


class DisjointSet:
    def __init__(self, n):
        self.disjoint_set = [-1 for _ in range(n + 1)]
        self.disjoint_set[0] = float('-inf')
        self.cycle = None
    
    def find(self, vertex):
        while self.disjoint_set[vertex] > 0:
            vertex = self.disjoint_set[vertex]
        return vertex
    
    def union(self, edge):
        u, v = edge
        s1 = self.find(u)
        s2 = self.find(v)
        if s1 != s2:
            if self.disjoint_set[s1] <= self.disjoint_set[s2]:
                self.disjoint_set[s1] -= self.disjoint_set[s2]
                self.disjoint_set[s2] = s1
            else:
                self.disjoint_set[s2] -= self.disjoint_set[s1]
                self.disjoint_set[s1] = s2 
        else:
            self.cycle = edge 
            
class Solution:
    def findRedundantConnection(self, edges):
        vertices = set()
        for u, v in edges:
            vertices.add(u)
            vertices.add(v)
        
        # number of dsitinct vertices 
        n = len(vertices)
        disjoint_set = DisjointSet(n)
    
        for edge in edges:
            disjoint_set.union(edge)
            
        return disjoint_set.cycle

#########################################################################
# other solution
#########################################################################

edges = [[1,2],[2,3],[3,4],[1,5]]

nodes = set()
for u,v in edges:
    nodes.add(u)
    nodes.add(v)

n = len(nodes)
parent = [v for v in range(n+1)]
rank = [1 for _ in range(n+1)]

def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])

def union(x,y):
    xroot = find(x)
    yroot = find(y)
    if xroot == yroot:
        return True
    else:
        if rank[xroot] >= rank[yroot]:
            parent[yroot] = xroot
            rank[xroot] += rank[yroot]
        else:
            parent[xroot] = yroot
            rank[yroot] += rank[xroot]
        return False

def isCyclePresent(edges):
    for u,v in edges:
        if union(u,v):
            return [u,v]