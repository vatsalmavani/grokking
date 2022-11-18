# LC: https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/
# solution: https://youtu.be/elADMOC_hDI
# other explanation: https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/discuss/303750/JavaC%2B%2BPython-Find-the-Subarray-with-Target-Sum
# other other explanation: https://youtu.be/i5UoDZbQ94Q?t=801


def submatrix_sum_target(matrix, target):
    row = len(matrix)
    col = len(matrix[0])

    # find prefix sum of all rows
    for i in range(row):
        for j in range(1,col):
            matrix[i][j] += matrix[i][j-1]

    res = 0
    for c1 in range(col):
        for c2 in range(c1, col):
            curSum = 0
            prefixSum_dict = {0:1}
            for r in range(row):
                curSum += matrix[r][c2] - (matrix[r][c1-1] if c1 > 0 else 0)
                if curSum - target in prefixSum_dict:
                    res += prefixSum_dict[curSum - target]
                prefixSum_dict[curSum] = prefixSum_dict.get(curSum,0) + 1
    return res


matrix = [[0,1,0], [1,1,1], [0,1,0]]
print(submatrix_sum_target(matrix, 0))

# time: O(n*m*m); n = rows; m = cols
# space: O(1)