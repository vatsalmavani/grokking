# kahn's algorithm is BFS implementation
# time complexity is O(V + E)

ipt = [[1,2], [1,3], [1,7], [2,3], [4,3], [4,1], [5,3], [6,1], [6,3], [8,1], [9,7], [9,8]]

graph = {}
visited = {}
indegree = {}
n = 9

for i in range(1, n+1):
    graph[i] = []
    visited[i] = False
    indegree[i] = 0

for (u,v) in ipt:
    graph[u].append(v)
    indegree[v] += 1

print(graph)
print(visited)
print(indegree)

def kahn(graph, visited, indegree):
    queue = []
    # adding nodes with 0 indegree to the queue
    for k, v in indegree.items():
        if v == 0:
            queue.append(k)
            visited[k] = True
    # same as bfs code
    while queue: # while queue is not empty
        deVertex = queue.pop(0)
        print(deVertex, end=" ")
        for child in graph[deVertex]:
            if not visited[child]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
                    visited[child] = True

kahn(graph, visited, indegree)