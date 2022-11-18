# https://www.youtube.com/watch?v=PXH5gcpM7l0&list=PLdylWCIGC6gebPnAqkoFNbij9bBHbX8__&index=20

grid = [[0,1,0,0,0,0],
        [0,1,0,0,0,0],
        [1,0,1,0,1,1],
        [0,0,1,1,0,0],
        [1,0,0,1,0,0],
        [1,1,0,1,0,0]]
    
row = len(grid)
col = len(grid[0])

visited = []
for i in range(row):
    temp = []
    for j in range(col):
        temp.append(0)
    visited.append(temp)

def isValid(grid, visited, i,j):
    if i<0 or j<0 or i>=row or j>=col or visited[i][j] == 1 or grid[i][j] == 1:
        return False
    return True

def dfs(grid, visited, i=0, j=0):
    visited[i][j] = 1
    sm = 0  # sum or no of nodes
    for child_i, child_j in [[i+1,j], [i-1,j], [i,j+1], [i,j-1]]:
        if isValid(grid, visited, child_i, child_j):
            sm += dfs(grid, visited, child_i, child_j)
    return sm + 1

answer = []
for i in range(row):
    for j in range(col):
        if visited[i][j] == 0 and grid[i][j] == 0:
            temp = dfs(grid, visited, i, j)
            answer.append(temp)

print(answer)