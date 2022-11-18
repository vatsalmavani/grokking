from collections import defaultdict


adj_matrix = [[1,1,1,0],
              [1,1,1,1],
              [1,1,1,0],
              [0,1,0,1]]

n = len(adj_matrix)     # no of nodes
adj_list = {}
for i in range(n):
    adj_list[i] = []
for i in range(n):
    for j in range(n):
        if i != j and adj_matrix[i][j] == 1:
            adj_list[i].append(j)
            # do NOT write this line otherwise every element will come twice
            # adj_list[j].append(i)

print(adj_list)

n = len(adj_matrix)
graph = defaultdict(list)
for i in range(n):
    for j in range(i+1,n):
        if adj_matrix[i][j] == 1:
            graph[i].append(j)
            graph[j].append(i)
print(graph)