# question: https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        row = len(board)
        col = len(board[0])
        
        def dfs(i,j):
            if 0<=i<row and 0<=j<col and board[i][j] == 'O':
                board[i][j] = 'T'
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)
        
        for i in [0, row-1]:
            for j in range(col):
                dfs(i,j)
            
        for i in range(row):
            for j in [0, col-1]:
                dfs(i,j)
                
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                    
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'T':
                    board[i][j] = 'O'




board = [["X","X","X","X"],
         ["X","O","O","X"],
         ["X","X","O","X"],
         ["X","O","X","X"]]

row = len(board)
col = len(board[0])

border = [(0,i) for i in range(col)] + [(row-1, i) for i in range(col)] +\
         [(i,0) for i in range(row)] + [(i,col-1) for i in range(row)]

# visited =set()
def dfs(start):
    i,j = start[0], start[1]
    board[i][j] = 'T'
    # visited.add(start)
    for ci,cj in [[i+1,j], [i-1,j], [i,j+1], [i,j-1]]:
        if 0<=ci<row and 0<=cj<col and board[ci][cj] == 'O':
            dfs((ci,cj))

for item in border:
    # if item not in visited:
    if board[item[0]][item[1]] == 'O':
        dfs(item)

# for i,j in visited:
#     board[i][j] = 'T'

for i in range(row):
    for j in range(col):
        if board[i][j] == 'O':
            board[i][j] = 'X'

for i in range(row):
    for j in range(col):
        if board[i][j] == 'T':
            board[i][j] = 'O'

for item in board:
    print(item)