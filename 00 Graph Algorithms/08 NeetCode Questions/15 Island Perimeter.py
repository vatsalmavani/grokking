# https://leetcode.com/problems/island-perimeter/


def islandPerimeter(grid) -> int:
    row = len(grid)
    col = len(grid[0])
    
    visited = set()
    def dfs(i,j):
        if i<0 or j<0 or i>=row or j>=col or grid[i][j] == 0:
            return 1
        if (i,j) in visited:
            return 0
        
        perim = 0
        visited.add((i,j))
        perim += dfs(i+1,j)
        perim += dfs(i-1,j)
        perim += dfs(i,j+1)
        perim += dfs(i,j-1)
        
        return perim
    
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                return dfs(i,j)

# time complexity is O(m*n) since we have to traverse entire matrix to find island; m = no of rows; n = no of cols
# also, time comp of DFS if O(V + E); V = no of vertices; E = no of edges in graph
# in matrix, there are M*N elements or vertices and (M-1)*(N-1) edges
# hence, O(V+E) becomes O(M*N + (M-1)*(N-1)) = O(2*M*N) = O(M*N)

def perim(grid):
    row = len(grid)
    col = len(grid[0])
    visited = set()
    per = 0
    def dfs(i,j):
        nonlocal per
        visited.add((i,j))
        for ci,cj in [[i+1,j], [i-1,j], [i,j+1], [i,j-1]]:
            if ci < 0 or ci >= row or cj < 0 or cj >= col or grid[ci][cj] == 0:
                per += 1
            if 0<=ci<row and 0<=cj<col and (ci,cj) not in visited and grid[ci][cj] == 1:
                dfs(ci,cj)
        return per
    for i in range(row):
        for j in range(col):
            if (i,j) not in visited and grid[i][j] == 1:
                return dfs(i,j)

# --------------------------------------------------------------------------

from collections import deque


def bfs_implementation(grid):
    row = len(grid)
    col = len(grid[0])

    queue = deque()
    visited = set()
    def bfs(i,j):
        res = 0
        while queue:
            x,y = queue.popleft()
            for xx,yy in [[x+1,y], [x-1,y], [x,y+1], [x,y-1]]:
                if xx < 0 or xx >= row or yy < 0 or yy >= col or grid[xx][yy] == 0:
                    res += 1
                if 0<=xx<row and 0<=yy<col and (xx,yy) not in visited and grid[xx][yy] == 1:
                    queue.append((xx,yy))
                    visited.add((xx,yy))
        return res
    

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                queue.append((i,j))
                visited.add((i,j))
                return bfs(i,j)


grid = [[1]]
print(bfs_implementation(grid))
grid = [[0,1,0,0],
        [1,1,1,0],
        [0,0,0,0],
        [0,0,0,0]]
print(bfs_implementation(grid))