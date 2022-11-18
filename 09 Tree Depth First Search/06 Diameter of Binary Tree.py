# LC: https://leetcode.com/problems/diameter-of-binary-tree/
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743963987_59Unit
# neetcode: https://youtu.be/bkxqA8Rfv04

# understand neetcode's solution for this code
def diameter(root):
    maxDia = 0
    def dfs(root):
        if not root:
            return -1
        left = dfs(root.left)
        right = dfs(root.right)

        nonlocal maxDia
        maxDia = max(maxDia, 2 + left + right)
        maxHeight = 1 + max(left, right)

        return maxHeight
    dfs(root)
    return maxDia