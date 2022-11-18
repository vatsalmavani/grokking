# bfs implementation is used for unweighted graph's sssp (single source shortest path)
# dijkstra is used for weighted graph's sssp (both - directed and undirected graphs)

# we are using greedy method to choose the MINIMUM cost node first
# and whenever we have minimum or maximum, heap should be the first thing in your mind
# so, dijkstra uses heap data structure in its application

# how does dijkstra algo work for undirected graphs?
# https://www.udemy.com/course/data-structures-and-algorithms-bootcamp-in-python/learn/lecture/22110066#overview

# how does dijkstra algo work for directed graphs?
# https://www.udemy.com/course/data-structures-and-algorithms-bootcamp-in-python/learn/lecture/32881816#overview

# this algo is from this video:
# https://www.youtube.com/watch?v=oRwrtfSl81c&list=PLdylWCIGC6gebPnAqkoFNbij9bBHbX8__&index=28

# bfs for sssp vs dijkstra
# search on youtube 'codecap dijkstra' and see why visited comes immediately after heappop and not after appending the element to the queue
# search on youtube 'codecap sssp' and see why visited comes immediately after we append the node to the queue as opposed to adding the element to the visited set after popping it


from heapq import *


ipt = [[0,1,6], [0,2,1], [1,2,2], [1,3,1], [1,4,2], [2,3,1], [3,4,2]]

graph = {}
n = 5
distance = {}
visited = {}

for i in range(n):
    graph[i] = []
    distance[i] = float('inf')
    visited[i] = False

for u,v,d in ipt:
    # note that dijkstra works for both directed and undirected, weighted graphs
    # here, we are making undirected graph by using both graph[u].append([d,v]) and graph[v].append([d,u]) statements
    # but if the graph was directed, ie only graph[u].append([d,v]) statement was used, it would work just fine
    graph[u].append([d,v])
    graph[v].append([d,u])

start = 0

def dijkstra(graph, start, visited, distance):
    distance[start] = 0
    heap = []
    heappush(heap, [0, start])  # heap is [distance, node] and distance of start from itself is 0
    while heap:     # while heap is not empty
        dist, node = heappop(heap)
        visited[node] = True
        for neib_dist, neib_node in graph[node]:    # neighbour_distance, neighbour_node
            # see that graph[u].append([d,v]) --> first is distance, second is node
            if not visited[neib_node] and distance[node] + neib_dist < distance[neib_node]:
                distance[neib_node] = distance[node] + neib_dist
                heappush(heap, [distance[neib_node], neib_node])
                # note: this heappush pushes some (in this case, node 1) more than once. But it doesn't matter since the node will be already visited and the if condition won't execute
                # (see python tutor for visualization)

dijkstra(graph, start, visited, distance)
print(distance)