# LC: https://leetcode.com/problems/path-sum-ii/
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743930963_55Unit
# deepti: https://youtu.be/Z2Q6UsVIyxY

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def f(root, target):
    res = []
    if not root: return res

    def dfs(root, target, ls, res):
        if not root:
            return
        if not root.left and not root.right and root.val == target:
            res += [ls + [root.val]]
        dfs(root.left, target - root.val, ls + [root.val], res)
        dfs(root.right, target - root.val, ls + [root.val], res)

        return res

    return dfs(root, target, [], [])

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)
f(root, 22)


##### deepti soltion #####

def helper(root, sum_tot, lst, result):
    if root.left is None and root.right is None:
        if root.val == sum_tot:
            result += [lst + [root.val]]
    if root.left:
        helper(root.left, sum_tot - root.val, lst + [root.val], result)
    if root.right:
        helper(root.right, sum_tot - root.val, lst + [root.val], result)
    return result

def pathSum(root, targetSum):
    if not root: return []
    return helper(root, targetSum, [], [])

root = TreeNode(0, TreeNode(1, TreeNode(3)), TreeNode(2, TreeNode(4), TreeNode(5)))
print(pathSum(root, 6))