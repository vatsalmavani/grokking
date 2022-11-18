# LC: https://leetcode.com/problems/detect-cycles-in-2d-grid/
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_62d679f1e93e0Unit
# sol: https://www.youtube.com/watch?v=eQvsVEt_j8M

# how to detect cycle?
# when we come across a visited node which is not current node's parent, it means there's a cycle





# dfs implementation (bfs implementation at the end)
from collections import deque

# using nonlocal variable
def detect_cycle(grid):
    row = len(grid)
    col = len(grid[0])
    visited = [[False]*col for _ in range(row)]

    found_cycle = False
    def dfs(i,j, pi, pj):   # previous i and previous j or parent i, j
        visited[i][j] = True
        nonlocal found_cycle    # don't use 'global' instead of nonlocal
        for ni,nj in [[i+1,j], [i-1,j], [i,j+1], [i,j-1]]:  # new i and new j
            if 0 <= ni < row and 0 <= nj < col and grid[ni][nj] == grid[i][j] and not (ni == pi and nj == pj):
                # grid[ni][nj] == grid[i][j] means the letters are same in both cells
                # not (ni == pi and nj == pj) means new i,j are pointing to the parent
                if visited[ni][nj]:
                    found_cycle = True
                else:
                    dfs(ni, nj, i,j)
    
    for i in range(row):
        for j in range(col):
            if not visited[i][j] and not found_cycle:
                dfs(i,j,-1,-1)
    
    return found_cycle


# note: this algo doesn't work. think why?
def cycle(grid):
    visited = set()
    def dfs(x,y, px,py):
        visited.add((x,y))
        for i,j in [[x+1,y], [x-1,y], [x,y+1], [x,y-1]]:
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j] == grid[x][y] and (i != px or j != py):
                if (i,j) in visited: return True
                else: dfs(i,j, x,y)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i,j) not in visited and dfs(i,j, -1,-1):    # note that order matters here bcoz if not visited, then only do dfs
                return True
    return False

grid = [["c","a","d"],
        ["a","a","a"],
        ["a","a","d"],
        ["a","c","d"],
        ["a","b","c"]]
print(cycle(grid))

# here, the answer should be true but we are getting False
# this is bcoz when we return True in dfs, it is returned to the parent dfs of that dfs call
# this True is not returned to the dfs we called in the two for loops
# basically whatever you return in the recursive call, it is returned to one layer up (parent) of that recursive call in the stack memory

# visualize this in python tutor slowly if you didn't get it



# other way to write it: since using nonlocal and global is not best practice
# this might be helpful: https://stackoverflow.com/questions/73674938/how-to-return-truth-value-to-the-base-function-in-recursion/73674971#73674971
def detect_cycle(grid):
    row = len(grid)
    col = len(grid[0])
    visited = [[False]*col for _ in range(row)]

    def dfs(i,j, pi, pj):
        visited[i][j] = True
        for x,y in [[i+1,j], [i-1,j], [i,j+1], [i,j-1]]:
            if 0 <= x < row and 0 <= y < col and grid[x][y] == grid[i][j] and not (x == pi and y == pj):
                if visited[x][y]:
                    return True
                elif dfs(x, y, i,j):
                    return True
        return False
    
    for i in range(row):
        for j in range(col):
            if not visited[i][j]:
                if dfs(i,j,-1,-1):
                    return True
    
    return False

grid = [["c","a","d"],
        ["a","b","a"],
        ["a","a","d"],
        ["a","c","d"],
        ["a","b","c"]]
print(detect_cycle(grid))

# using this way makes sure that whenever dfs returns True, it is directly sent to the upper most parent



############################################################################



# bfs implementation:

from collections import deque


def detect(grid):
    visited = set()
    def bfs(i,j, pi, pj):
        queue = deque([(i,j, pi, pj)])
        visited.add((i,j))
        while queue:
            x,y, px,py = queue.popleft()
            for xx,yy in [[x+1,y], [x-1,y], [x,y+1], [x,y-1]]:
                if 0 <= xx < len(grid) and 0 <= yy < len(grid[0]) and (xx != px or yy != py) and grid[xx][yy] == grid[x][y]:
                    if (xx,yy) in visited:
                        return True
                    else:
                        queue.append((xx,yy,x,y))
                        visited.add((xx,yy))
        return False
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i,j) not in visited:
                if bfs(i,j,-1,-1): return True
    return False

grid = [["b","b","b"],["b","z","b"],["b","b","b"]]
print(detect(grid))