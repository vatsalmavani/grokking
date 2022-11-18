# premium question, hence video: https://youtu.be/8f1XPm4WOUc
# alternative: https://leetcode.com/problems/number-of-provinces/

from collections import defaultdict


edges = [[0,1], [1,2], [3,4]]
# edges = [['a','b'], ['a','c'], ['a','d'], ['b','e'], ['d','e'],
#          ['f','h'], ['f','g'],
#          ['i','j']]

graph = {}
nodes = set()
visited = set()
for u,v in edges:
    nodes.add(u)
    nodes.add(v)
for i in nodes:
    graph[i] = []
for u,v in edges:
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph, visited, node):
    visited.add(node)
    for nbr in graph[node]:
        if nbr not in visited:
            dfs(graph, visited, nbr)

count = 0
for node in nodes:
    if node not in visited:
        dfs(graph, visited, node)
        count += 1
    
print(count)


# number-of-provinces

def f(grid):
    n = len(grid)
    graph = defaultdict(list)
    for i in range(n):
        for j in range(i,n):    # don't write range(i+1,n)
            if grid[i][j] == 1:
                graph[i+1].append(j+1)
                graph[j+1].append(i+1)
    
    visited = set()
    def dfs(node):
        visited.add((node))
        for child in graph[node]:
            if child not in visited:
                dfs(child)
    
    count = 0
    for node in graph:
        if node not in visited:
            count += 1
            dfs(node)
    
    return count