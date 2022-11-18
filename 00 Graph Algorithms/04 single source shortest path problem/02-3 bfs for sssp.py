# https://www.youtube.com/watch?v=wBW1GGvpJGc&list=PLdylWCIGC6gebPnAqkoFNbij9bBHbX8__&index=13
# finding minimum distance of each node from a given node in an undirected graph

# bfs for sssp vs dijkstra
# search on youtube 'codecap dijkstra' and see why visited comes immediately after heappop and not after appending the element to the queue
# search on youtube 'codecap sssp' and see why visited comes immediately after we append the node to the queue as opposed to adding the element to the visited set after popping it


ipt = [[1,2], [1,3], [1,7], [2,3], [4,3], [4,1], [5,3], [6,1], [6,3], [8,1], [9,7], [9,8]]

graph = {}
distance = {}
n = 9

for i in range(1, n+1):
    graph[i] = []
    distance[i] = -1
for u,v in ipt:
    graph[u].append(v)
    graph[v].append(u)

def bfs(graph, source, distance: dict):
    queue = [source]
    visited = [source]
    # distance of starting node from itself is zero
    distance[source] = 0
    while queue:
        deVertex = queue.pop(0)
        for neighbour in graph[deVertex]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)
                # distance of child node is 1 plus distance of parent node
                distance[neighbour] = distance[deVertex] + 1
    
bfs(graph, 1, distance)
print(distance)

##### OR #####

from collections import defaultdict, deque


ipt = [[1,2], [1,3], [1,7], [2,3], [4,3], [4,1], [5,3], [6,1], [6,3], [8,1], [9,7], [9,8]]

graph = defaultdict(list)
distance = {}
for u,v in ipt:
    graph[u].append(v)
    graph[v].append(u)
    distance[u] = float('inf')
    distance[v] = float('inf')

def f(source):
    q = deque([source])
    visited = set([source])
    distance[source] = 0
    while q:
        deVertex = q.popleft()
        for child in graph[deVertex]:
            if child not in visited and distance[child] > distance[deVertex] + 1:
                distance[child] = distance[deVertex] + 1
                q.append(child)
                visited.add(child)
    return distance

print(f(1))