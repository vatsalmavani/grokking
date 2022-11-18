# note: generally in graph problems, input is given like the first file
# but in case graph is directly given as adjacency list, we have to find indegree
# https://www.youtube.com/watch?v=E5LEkIOUA54&list=PLdylWCIGC6gebPnAqkoFNbij9bBHbX8__&index=14

graph = {1: [2, 3, 7], 2: [3], 3: [], 4: [3, 1], 5: [3], 6: [1, 3], 7: [], 8: [1], 9: [7, 8]}

def kahn(graph, noOfNodes):
    # calculating indegree
    indegree = {}
    for key in graph:
        indegree[key] = 0
    for vertex in range(1, noOfNodes+1):
        for neighbour in graph[vertex]:
            indegree[neighbour] += 1
    print(indegree)

    # or
    # indegree = {}
    # for i in range(1, n+1):
    #     indegree[i] = 0
    # for k,v in graph.items():
    #     for value in v:
    #         indegree[value] += 1
    # print(indegree)

    # kahn's code
    queue = []
    visited = []
    for k,v in indegree.items():
        if v == 0:
            queue.append(k)
            visited.append(k)
    while queue:
        deVertex = queue.pop(0)
        print(deVertex, end=" ")
        for neighbour in graph[deVertex]:
            if neighbour not in visited:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
                    visited.append(neighbour)


n = len(graph.keys())
kahn(graph, n)