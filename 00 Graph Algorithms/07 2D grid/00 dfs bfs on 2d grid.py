grid = [[1,2,3,10],
        [4,5,6,11],
        [7,8,9,12]]

visited = set()

def dfs(grid, visited, start):
    i,j = start[0], start[1]
    print(grid[i][j])
    visited.add(start)
    for ci, cj in [[i+1,j], [i-1,j], [i,j+1], [i,j-1]]:
        if (ci,cj) not in visited and 0<=ci<len(grid) and 0<=cj<len(grid[0]):
            dfs(grid, visited, (ci,cj))
    
def bfs(grid, visited, start):
    queue = [start]
    visited.add(start)
    while queue:
        di, dj = queue.pop(0)
        print(grid[di][dj])
        for ci, cj in [[di+1,dj], [di-1,dj], [di,dj+1], [di,dj-1]]:
            if (ci,cj) not in visited and 0<=ci<len(grid) and 0<=cj<len(grid[0]):
                queue.append((ci,cj))
                visited.add((ci,cj))

bfs(grid, visited, (0,0))