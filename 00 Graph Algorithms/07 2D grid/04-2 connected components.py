# https://www.youtube.com/watch?v=VMgp6hlls-A&list=PLdylWCIGC6gebPnAqkoFNbij9bBHbX8__&index=3

edges = [['a','b'], ['a','c'], ['a','d'], ['b','e'], ['d','e'],
         ['f','h'], ['f','g'],
         ['i','j']]
nodes = ['a','b','c','d','e','f','g','h','i','j','k']

visited = []
graph = {}
for i in nodes:
    graph[i] = []
for u,v in edges:
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph, node, visited):
    # print(node)
    visited.append(node)
    v = 0    # v = no of nodes
    for child in graph[node]:
        if child not in visited:
            v += dfs(graph, child, visited)
    return v + 1

answer = []
for item in nodes:
    if item not in visited:
        temp = dfs(graph, item, visited)
        answer.append(temp)
    
print(answer)