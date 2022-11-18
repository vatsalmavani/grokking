# https://www.youtube.com/watch?v=b68dqjrVISE&list=PLdylWCIGC6gebPnAqkoFNbij9bBHbX8__&index=17

grid = [[1,2,3],
        [4,5,6],
        [7,8,9]]

row = len(grid)
col = len(grid[0])

visited = []
for i in range(row):
    temp = []
    for j in range(col):
        temp.append(0)
    visited.append(temp)

start = (0,0)
def bfs(grid, visited, start):
    queue = [start]
    si, sj = start[0], start[1]
    visited[si][sj] = 1
    while queue:
        dei, dej = queue.pop(0)     # deVertex i and deVertex j
        print(grid[dei][dej])
        for child_i, child_j in [[dei+1,dej], [dei-1,dej], [dei,dej+1], [dei,dej-1]]:
            if isValid(grid, visited, child_i, child_j):
                queue.append((child_i, child_j))
                visited[child_i][child_j] = 1

def isValid(grid, visited, x, y):
    if x < 0 or y < 0 or x >= row or y >= col or visited[x][y] == 1:
        return False
    return True

bfs(grid, visited, start)