ipt = [[1,2], [1,3], [1,4], [1,5], [2,5], [2,7], [3,7], [3,4], [3,8], [5,6], [5,9], [9,10]]

graph = {}
for i in range(1,11):
    graph[i] = []
print(graph)

for u,v in ipt:
    graph[u].append(v)
    graph[v].append(u)
print(graph)

# non-recursive implementation
def dfs(graph, source):
    visited = [source]
    stack = [source]
    while stack:
        popVertex = stack.pop()
        print(popVertex, end=" ")
        for neighbour in graph[popVertex]:
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)

dfs(graph, 1)

# recursive implementation
def dfsRecursive(graph, source, visited=[]):
    visited.append(source)
    print(source, end=" ")
    for child in graph[source]:
        if child not in visited:
            dfsRecursive(graph, child, visited)

print()
dfsRecursive(graph, 1)