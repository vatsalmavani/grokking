# https://www.youtube.com/watch?v=RXfAFPYM94g&list=PLdylWCIGC6gebPnAqkoFNbij9bBHbX8__&index=17

grid = [[1,2,3], [4,5,6], [7,8,9]]

row = len(grid)
col = len(grid[0])

visited = []
for i in range(row):
    temp = []
    for j in range(col):
        temp.append(0)
    visited.append(temp)
# print(visited)

start = (0,0)   # starts from 1
def dfs(grid, visited, start):
    i,j = start[0], start[1]    # start is a tuple so start[0] is i and start[1] is j
    print(grid[i][j])
    visited[i][j] = 1
    for u,v in [[i+1,j], [i-1,j], [i,j+1], [i,j-1]]:
        # [i+1,j] = upper element
        # [i-1,j] = bottom element
        # [i,j+1] = right element
        # [i,j-1] = left element
        # basically, for neibour in [lists] where u = neighbour[0], v = neighbour[1]
        if isValid(grid, visited, u, v):
            dfs(grid, visited, (u,v))

def isValid(grid, visited, x, y):
    row = len(grid)
    col = len(grid[0])
    if x < 0 or y < 0 or x >= row or y >= col or visited[x][y] == 1:
        return False
    return True

dfs(grid, visited, start)