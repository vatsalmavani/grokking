# LC premium problem 694
# lintcode: https://www.lintcode.com/problem/860/
# solution approach: https://www.youtube.com/watch?v=u617H2WwR5g

# grokking's dfs implementation (if you wanna see): https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_62d679f3bf35bUnit

from collections import deque

'''
def distinct_island(grid):
    row = len(grid)
    col = len(grid[0])
    visited = set()
    shapes = set()

    def bfs(i,j):
        queue = deque([(i,j)])
        visited.add((i,j))
        shape = "00"
        while queue:
            i,j = queue.popleft()
            for ci,cj in [[i+1,j], [i-1,j], [i,j+1], [i,j-1]]:
                if 0<=ci<row and 0<=cj<col and (ci,cj) not in visited and grid[ci][cj] == 1:
                    queue.append((ci,cj))
                    visited.add((ci,cj))
                    ##############################################
                    # this small mistake gives wrong ans sometimes
                    shape += str(ci-i) + str(cj-j)
                    ##############################
        shapes.add(shape)
    
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1 and (i,j) not in visited:
                bfs(i,j)
            
    return len(shapes)

grid = [[1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,0,1,1],
        [0,0,0,1,1]]

print(distinct_island(grid))
'''

# "find distinct" = use hash set or hash table

def numberof_distinct_islands(grid):
    # write your code here
    row = len(grid)
    col = len(grid[0])
    visited = set()
    shapes = set()
    def bfs(x,y):
        queue = deque([(x,y)])
        visited.add((x,y))
        shape = "00"
        while queue:
            i,j = queue.popleft()
            for ci,cj in [[i+1,j], [i-1,j], [i,j+1], [i,j-1]]:
                if 0<=ci<row and 0<=cj<col and (ci,cj) not in visited and grid[ci][cj] == 1:
                    queue.append((ci,cj))
                    visited.add((ci,cj))
                    shape += str(ci-x) + str(cj-y)
        shapes.add(shape)
    
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1 and (i,j) not in visited:
                bfs(i,j)
            
    return len(shapes)

grid = [[1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,0,1,1],
        [1,0,0,1,1]]

print(numberof_distinct_islands(grid))