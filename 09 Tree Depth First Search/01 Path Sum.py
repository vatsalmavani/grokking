# LC: https://leetcode.com/problems/path-sum/
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743923908_54Unit

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def has_path(root, summ):
    if not root:
        return False
    if root.val == summ and not root.left and not root.right:
        return True
    return has_path(root.left, summ - root.val) or has_path(root.right, summ - root.val)

root = TreeNode(0, TreeNode(1, TreeNode(3)), TreeNode(2, TreeNode(4), TreeNode(5)))
print(has_path(root, 5))

# traversing each node once. hence time complexity: O(n)
# if the tree is a linked list (every node has only one child)
# then recursion stack memory will have to store all nodes
# hence space complexity is O(n)