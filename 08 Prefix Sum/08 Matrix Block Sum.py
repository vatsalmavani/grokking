# LC: https://leetcode.com/problems/matrix-block-sum/
# solution: https://leetcode.com/problems/matrix-block-sum/discuss/482730/PythonJSGoC%2B%2B-O(-m*n-)-Integral-Image-DP-w-Explanation

# note that this problem uses exactly the same concept as the previous preblem

def matrixBlockSum(mat, K):
        
    rows, cols = len(mat), len(mat[0])
    integral_image = [ [0]*cols for _ in range(rows) ]
    
    # building integral image to speed up block sum computation
    for r in range(rows):
        presum = 0
        for c in range(cols):
            presum += mat[r][c]
            above = mat[r-1][c] if r > 0 else 0
            integral_image[r][c] = presum + above
    
    
    # compute block sum by looking-up integral image
    output_image = [ [0]*cols for _ in range(rows) ]
    
    for r in range(rows):
        for c in range(cols):
            
            min_row, max_row = max(0, r-K), min(rows-1, r+K)
            min_col, max_col = max(0, c-K), min(cols-1, c+K)
            
            output_image[r][c] = integral_image[max_row][max_col]
            
            if min_row > 0:
                output_image[r][c] -= integral_image[min_row-1][max_col]
            
            if min_col > 0:
                output_image[r][c] -= integral_image[max_row][min_col-1]
                
            if min_col > 0 and min_row > 0:
                output_image[r][c] += integral_image[min_row-1][min_col-1]
            
    return output_image