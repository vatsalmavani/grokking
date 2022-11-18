# codecap (2nd method using graph traversal): https://youtu.be/UFVD71TNo-U?list=PLdylWCIGC6gebPnAqkoFNbij9bBHbX8__
# codecap implementation better than neetcode but it has a bug in the video. following code is correct

# method 1: union find

def isCyclePresent(n, edges):
    parent = {i:i for i in range(n)}
    rank = dict.fromkeys(range(n), 1)

    def findParent(node):
        if parent[node] == node:
            return node
        return findParent(parent[node])

    def union(x, y):
        xroot = findParent(x)
        yroot = findParent(y)
        if xroot != yroot:
            if rank[xroot] >= rank[yroot]:
                parent[yroot] = xroot
                rank[xroot] += rank[yroot]
            else:
                parent[xroot] = yroot
                rank[yroot] += rank[xroot]
            return True     # true bcoz union happened
        return False    # false bcoz union didn't happen and hence there is a cycle

    for u,v in edges:
        if not union(u,v):
            return True # cycle IS present
    return False    # no cycle



# method 2: graph traversal (same as cycle detection in 2d grid)
from collections import defaultdict


def cycleDetection(n, edges):
    graph = defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = set()
    def dfs(node, prev):
        visited.add(node)
        for child in graph[node]:
            if child not in visited:
                if dfs(child, node):
                    return True     # we don't need else: False condition bcoz if this condition (if dfs) isn't stisfied, python will jump to the last line of this funcn --> return False
            else:   # child in visited
                if child == prev:   # previous node is always in visited
                    continue
                else:   # not previous but still visited. cycle detected
                    return True
        return False
    
    return dfs(0,-1)


# visualize in python tutor to understand recursion (first draw the graph in whiteboard)
n = 7
edges = [[0,1], [0,4], [1,2], [1,3], [4,5], [4,6], [5,6]]
print(cycleDetection(n, edges))