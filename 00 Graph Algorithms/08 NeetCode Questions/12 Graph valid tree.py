# if you don't understand the logic, watch the geeks for geeks video on detecting a cycle using union find
# https://www.youtube.com/watch?v=mHz-mx-8lJ8&t=355s
# https://www.lintcode.com/problem/178/
# neetcode (this code): https://youtu.be/bXsUuownnoQ

from collections import defaultdict


edges1 = [[0, 1], [0, 2], [0, 3], [1, 4]]
n1 = 5
edges2 = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
n2 = 5
edges3 = [[0,1], [1,2], [2,3], [3,4], [4,0]]
n3 = 5
edges4 = [[0,1], [1,2], [0,2], [2,3], [3,4], [4,2]]
n4 = 5
edges5 = [[0,1], [0,4], [1,2], [1,3], [3,5], [3,6]]
n5 = 7

def isCyclePresent(n, edges):
    parent = [v for v in range(n)]
    rank = [1 for i in range(n)]

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
            return True
    return False

print(isCyclePresent(n1,edges1))
print(isCyclePresent(n2,edges2))
print(isCyclePresent(n3,edges3))
print(isCyclePresent(n4,edges4))
print(isCyclePresent(n5,edges5))



############### BUT ###############
# graph valid tree is not the problem about finding a cycle in a graph
# it is just part of it
# eg. n = 2, edges = []
# here, there are 2 nodes which are not connected and hence, it is not a valid tree
# this case is not statisfied by union find

def graphValidTree(n, edges):
    # two steps: detect cycle and check if all nodes are connected

    # empty graph is graph
    if not n: return True

    graph = defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # detect cycle
    visited = set()
    def dfs(node, prevNode):
        visited.add(node)
        for child in graph[node]:
            if child not in visited:
                if dfs(child, node):
                    return True
            else:   # child in visited
                if child == prevNode:   # previous node is always in visited
                    continue
                else:   # not previous but still visited. cycle detected
                    return True
        return False
    
    return not dfs(0, -1) and n == len(visited) # if n = visited.len then obviously all nodes are visited