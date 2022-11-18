# LC: https://leetcode.com/problems/sum-root-to-leaf-numbers/
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743939828_56Unit
# neetcode: https://youtu.be/Jk16lZGFWxE

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def path_nums(root):
    def dfs(root, path_sum):
        if not root:
            return 0
        path_sum = path_sum * 10 + root.val
        if not root.left and not root.right:
            return path_sum
        left = dfs(root.left, path_sum)
        right = dfs(root.right, path_sum)
        return left + right
    return dfs(root, 0)

root = TreeNode(0, TreeNode(1, TreeNode(3)), TreeNode(2, TreeNode(4), TreeNode(5)))
print(path_nums(root))

# time = space = O(n)