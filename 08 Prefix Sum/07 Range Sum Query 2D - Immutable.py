# LC: https://leetcode.com/problems/range-sum-query-2d-immutable/
# NC: https://youtu.be/KE8MQuwE2yA

class NumMatrix:
    def __init__(self, matrix):
        row, col = len(matrix), len(matrix[0])
        self.sumMat = [[0]*(col+1) for _ in range(row+1)]
        for r in range(row):
            prefix = 0
            for c in range(col):
                prefix += matrix[r][c]
                above = self.sumMat[r][c+1]
                self.sumMat[r+1][c+1] = prefix + above
    
    def sumRegion(self, r1, c1, r2, c2):
        r1, c1, r2, c2 = r1+1, c1+1, r2+1, c2+1
        bottomRight = self.sumMat[r2][c2]
        above = self.sumMat[r1-1][c2]
        left = self.sumMat[r2][c1-1]
        topLeft = self.sumMat[r1-1][c1-1]
        return bottomRight - above - left + topLeft


grid = [[1,0,0,1],
        [0,1,1,0],
        [0,1,0,1],
        [1,0,1,0]]

m = NumMatrix(grid)
for item in m.sumMat:
    print(item)

m.sumRegion(2,1,3,2)