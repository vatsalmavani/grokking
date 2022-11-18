# LC: https://leetcode.com/problems/number-of-closed-islands/
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_62d6145eebddeUnit

# just like pacific/atlantic ocean problem, we are gonna start from the boundary
# mark all islands connected to boundary as "connected to edge"
# the islands which are not "connected to edge" are surrounded by water


def countIsland(grid):
    visited = set()
    row = len(grid)
    col = len(grid[0])
    connectedToEdge = [[False for i in range(col)] for j in range(row)]
    
    def dfs(source, boolean):
        i,j = source[0], source[1]
        visited.add(source)
        connectedToEdge[i][j] = boolean
        for ci,cj in [[i+1,j], [i-1,j], [i,j+1], [i,j-1]]:
            if 0<=ci<row and 0<=cj<col and (ci,cj) not in visited and grid[ci][cj] == 1:
                dfs((ci,cj), boolean)
    
    for i in [0, row-1]:
        for j in range(col):
            if (i,j) not in visited and grid[i][j] == 1:
                dfs((i,j), True)
    
    for i in range(row):
        for j in [0,col-1]:
            if (i,j) not in visited and grid[i][j] == 1:
                dfs((i,j), True)

    count = 0
    for i in range(1,row-1):
        for j in range(1,col-1):
            if (i,j) not in visited and grid[i][j] == 1 and connectedToEdge[i][j] == False:
                dfs((i,j), False)
                count += 1
    
    return count

grid = [[1,1,0,0,0],
        [0,1,0,0,0],
        [0,0,1,1,0],
        [0,1,1,0,0],
        [0,0,0,0,0]]
    
print(countIsland(grid))