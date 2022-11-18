ipt = [[1,2], [1,3], [1,4], [1,5], [2,5], [2,6], [2,7], [3,4],
       [4,8], [4,9], [5,6], [5,9], [9,10]]
    
graph = {}
for i in range(1, 11):
    graph[i] = []
for u,v in ipt:
    graph[u].append(v)
    graph[v].append(u)

def bfs(graph, source):
    visited = [source]
    queue = [source]
    while queue:
        deVertex = queue.pop(0)
        print(deVertex, end=" ")
        for neighbour in graph[deVertex]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

bfs(graph, 1)