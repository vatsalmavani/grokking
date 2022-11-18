# q: https://leetcode.com/problems/walls-and-gates/
# q: https://youtu.be/e69C6xhiSQE

from collections import deque


grid = [[float('inf'), -1, 0, float('inf')],
        [float('inf'), float('inf'), float('inf'), -1],
        [float('inf'), -1, -1, -1],
        [0, -1, float('inf'), float('inf')]]

row = len(grid)
col = len(grid[0])
visited = set()
queue = deque()
for i in range(row):
    for j in range(col):
        if grid[i][j] == 0:
            queue.append((i,j))
            visited.add((i,j))

def bfs(grid, visited, queue):
    distance = 0
    while queue:
        for _ in range(len(queue)):
            i,j = queue.popleft()
            grid[i][j] = distance
            # this is basically level order traversal so in the first iteration, all the index with value 0 will be popped
            # in the 2nd iteration, all the first level rooms will be popped and so on
            for ii, jj in [[i+1,j], [i-1,j], [i,j+1], [i,j-1]]:
                if 0<=ii<row and 0<=jj<col and (ii,jj) not in visited and grid[ii][jj] != -1:
                    queue.append((ii,jj))
                    visited.add((ii,jj))
        distance += 1
        # we add distance += 1 here AFTER the outer for loop bcoz when outer for loop ends, rooms from both sides advances once
        # if you don't get it, read the previous image '06-3 why for range loop'

bfs(grid, visited, queue)
for item in grid:
    print(item)

########################################################################
# other way to put it
########################################################################

grid = [[float('inf'), -1, 0, float('inf')],
        [float('inf'), float('inf'), float('inf'), -1],
        [float('inf'), -1, -1, -1],
        [0, -1, float('inf'), float('inf')]]

queue = deque()
visited = set()

row = len(grid)
col = len(grid[0])

for i in range(row):
    for j in range(col):
        if grid[i][j] == 0:
            queue.append((i,j))
            visited.add((i,j))

while queue:
    for _ in range(len(queue)):
        i,j = queue.popleft()
        for x,y in [[i+1,j], [i-1,j], [i,j+1], [i,j-1]]:
            if 0<=x<row and 0<=y<col and grid[x][y] != -1 and (x,y) not in visited:
                queue.append((x,y))
                visited.add((x,y))
                grid[x][y] = grid[i][j] + 1

for item in grid:
    print(item)