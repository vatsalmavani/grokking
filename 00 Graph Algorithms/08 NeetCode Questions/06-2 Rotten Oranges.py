# question: https://leetcode.com/problems/rotting-oranges/

# go to this post if you don't understand why there are two for loops in bfs:
# https://www.reddit.com/r/leetcode/comments/wgp88l/leetcode_994_rotting_oranges/
# or go to the next image

import collections

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        
        fresh_count = 0
        time = 0
        queue = collections.deque()
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh_count += 1
                if grid[i][j] == 2:
                    queue.append([i,j])
        
        while queue and fresh_count > 0:
            # range(len(queue)) object is created at the start of the loop
            # hence, we are going level by level
            for i in range(len(queue)):
                r,c = queue.popleft()
                for x,y in [[r+1,c], [r-1,c], [r,c+1], [r,c-1]]:
                    if 0<=x<row and 0<=y<col and grid[x][y] == 1:
                        queue.append([x,y])
                        fresh_count -= 1
                        grid[x][y] = 2
            time += 1
        
        return time if fresh_count == 0 else -1