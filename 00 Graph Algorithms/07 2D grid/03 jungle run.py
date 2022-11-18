# https://www.youtube.com/watch?v=riz-rX-WRGQ&list=PLdylWCIGC6gebPnAqkoFNbij9bBHbX8__&index=19

grid = [['S','N','P','P','P'],
        ['P','P','P','N','P'],
        ['P','N','N','N','P'],
        ['P','N','E','P','P']]

row = len(grid)
col = len(grid[0])

visited = []
distance = []
for i in range(row):
    temp = []
    temp2 = []
    for j in range(col):
        temp.append(0)
        temp2.append(-1)
        if grid[i][j] == 'S':
            start = (i,j)
        if grid[i][j] == 'E':
            end = (i,j)
    visited.append(temp)
    distance.append(temp2)
# print(visited)
# print(distance)
# print(start)
# print(end)

def bfs(grid, visited, distance, start, end):
    queue = [start]
    distance[start[0]][start[1]] = 0
    visited[start[0]][start[1]] = 1
    while queue:
        i,j = queue.pop(0)  # since each element of queue is two element tuple
        for x,y in [[i+1,j], [i-1,j], [i,j+1], [i,j-1]]:
            if isValid(grid, visited, x, y):
                queue.append((x,y))
                visited[x][y] = 1
                distance[x][y] = distance[i][j] + 1
    return distance[end[0]][end[1]]

def isValid(grid, visited, x, y):
    if x < 0 or y < 0 or x >= row or y >= col or visited[x][y] == 1 or grid[x][y] == 'N':
        return False
    return True

print(bfs(grid, visited, distance, start, end))

for item in distance:
    print(item)