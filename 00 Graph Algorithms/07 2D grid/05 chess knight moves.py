# https://www.youtube.com/watch?v=2KstzDPtGYo&list=PLdylWCIGC6gebPnAqkoFNbij9bBHbX8__&index=21

# this is basically single source shortest path problem and hence dfs does not work
# more specifically, this is sssp on unweighted graph
# hence we will use bfs for the solution

grid = [['','B','',''],
        ['','','',''],
        ['','A','',''],
        ['','','','']]
    
child = [[-2,-1], [-2,1], [2,-1], [2,1], [-1,-2], [1,-2], [-1,2], [1,2]]

row = len(grid)
col = len(grid[0])

visited = []
distance = []
for i in range(row):
    t1 = []     # temp 1
    t2 = []     # temp 2
    for j in range(col):
        t1.append(0)
        t2.append(-1)
    visited.append(t1)
    distance.append(t2)

for i in range(row):
    for j in range(col):
        if grid[i][j] == 'A':
            start = (i,j)
        if grid[i][j] == 'B':
            end = (i,j)

def isValid(grid, visited, x, y):
    if x<0 or y<0 or x>=row or y>=col or visited[x][y] == 1:
        return False
    return True

def bfs(grid, visited, distance, start):
    queue = [start]
    visited[start[0]][start[1]] = 1
    distance[start[0]][start[1]] = 0
    while queue:
        i,j = queue.pop(0)
        for u, v in child:
            if isValid(grid, visited, i+u, j+v):
                queue.append((i+u, j+v))
                visited[i+u][j+v] = 1
                distance[i+u][j+v] = distance[i][j] + 1
    print(distance[end[0]][end[1]])


bfs(grid, visited, distance, start)
for item in distance:
    print(item)