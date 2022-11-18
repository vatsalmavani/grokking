# https://leetcode.com/problems/max-area-of-island/
# neetcode's solution is also pretty decent. check it out

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        
        visited = []
        for i in range(row):
            temp = []
            for j in range(col):
                temp.append(0)
            visited.append(temp)
        
        def isvalid(grid, visited, x, y):
            if x<0 or y<0 or x>=row or y>=col or grid[x][y]==0 or visited[x][y]==1:
                return False
            return True
        
        def bfs(grid, start):
            queue = [start]
            si, sj = start[0], start[1]
            sm = 0
            visited[si][sj] = 1
            while queue:
                di, dj = queue.pop(0)
                sm += 1
                for ci, cj in [[di+1,dj], [di-1,dj], [di,dj+1], [di,dj-1]]:
                    if isvalid(grid, visited, ci, cj):
                        queue.append((ci, cj))
                        visited[ci][cj] = 1
            return sm
        
        ans = []
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    temp = bfs(grid, (i,j))
                    ans.append(temp)
        
        return max(ans) if ans != [] else 0

############################################
# dfs solution
############################################

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

row = len(grid)
col = len(grid[0])

visited = set()
def dfs(source):
    i,j = source[0], source[1]
    visited.add((i,j))
    sm = 0
    for x,y in [[i+1,j], [i-1,j], [i,j+1], [i,j-1]]:
        if 0<=x<row and 0<=y<col and (x,y) not in visited and grid[x][y] == 1:
            sm += dfs((x,y))
    return sm +1

m = 0
for i in range(row):
    for j in range(col):
        if grid[i][j] == 1 and (i,j) not in visited:
            temp = dfs((i,j))
            m = max(m, temp)

print(m)