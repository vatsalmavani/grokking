# question: https://leetcode.com/problems/pacific-atlantic-water-flow/
# sol: https://leetcode.com/problems/pacific-atlantic-water-flow/discuss/2082292/Python-Breath-First-Search-twice

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

"""
Approach:

Do Breath First Search (BFS) twice

1. Collect all nodes that can reach Pacific ocean
    1a. Start BFS with all nodes on the left and top edges, all visited nodes in the traversal can reach Pacific Ocean. 
	1b. The neighbouring node must have an equal or higher height.
2. Collect all nodes that can reach Atlantic ocean
    2a. Start BFS with all nodes on the right and bottom edges, all visited nodes in the traversal can reach Atlantic Ocean.
	2b. The neighbouring node must have an equal or higher height.
3. Calculate the intersection of the two sets.

Time: O(|V| + |E|) = O(mn)
Space: O(|V|) = O(mn)
"""

from collections import deque

def pacificAtlantic(heights):
    row = len(heights)
    col = len(heights[0])
    
    pac_visited = set()
    atl_visited = set()
    
    def bfs(heights, visited, source):
        queue = deque()
        queue.append(source)
        visited.add(source)
        while queue:
            di, dj = queue.popleft()
            for ci, cj in [[di+1,dj], [di-1,dj], [di,dj+1], [di,dj-1]]:
                if 0<=ci<row and 0<=cj<col and (ci,cj) not in visited and heights[ci][cj] >= heights[di][dj]:
                    queue.append((ci,cj))
                    visited.add((ci,cj))
    
    pac_adj = [(0,c) for c in range(col)] + [(r,0) for r in range(row)]     # nodes adjacent to pacific ocean
    atl_adj = [(row-1, c) for c in range(col)] + [(r, col-1) for r in range(row)]   # node adjacent to atlantic ocean
    
    for i,j in pac_adj:
        bfs(heights, pac_visited, (i,j))
    for i,j in atl_adj:
        bfs(heights, atl_visited, (i,j))
        
    both_visited = pac_visited.intersection(atl_visited)
    return both_visited

print(pacificAtlantic(heights))