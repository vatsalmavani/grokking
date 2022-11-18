# https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        
        # creating adjacency list from adjacency matrix
        # here, since nodes start from 1 and matrix indices start from 0, approprite tweaks have to be made
        graph = {}
        for i in range(1, n+1):
            graph[i] = []
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    graph[i+1].append(j+1)
        
        visited = set()
        def dfs(visited, node):
            visited.add(node)
            for child in graph[node]:
                if child not in visited:
                    dfs(visited, child)
        
        count = 0
        for i in range(1, n+1):
            if i not in visited:
                dfs(visited, i)
                count += 1
        
        return count

from collections import defaultdict, deque


def f(grid):
    graph = defaultdict(list)
    row, col = len(grid), len(grid[0])
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1 and i != j:
                graph[i].append(j)
    
    visited = set()
    def bfs(node):
        queue = deque()
        queue.append(node)
        visited.add(node)
        while queue:
            deNode = queue.popleft()
            for child in graph[deNode]:
                if child not in visited:
                    queue.append(child)
                    visited.add(child)

    count = 0    
    for node in range(row):
        if node not in visited:
            count += 1
            bfs(node)
    return count

print(f([[1,1,0], [1,1,0], [0,0,1]]))