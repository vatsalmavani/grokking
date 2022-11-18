# LC: https://leetcode.com/problems/binary-tree-right-side-view/
# grokking (given better examples than leetcode): https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743902403_52Unit

# This problem follows the Binary Tree Level Order Traversal pattern. We can follow the same BFS approach.
# The only additional thing we will be doing is to append the last node of each level to the result array.

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_right_view(root):
    res = []
    if not root:
        return res
    queue = deque([root])
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if level_size == 1:
                res.append(node.val)
            level_size -= 1
    return res

root = TreeNode(0, TreeNode(1, TreeNode(3)), TreeNode(2, TreeNode(4), TreeNode(5)))
print(tree_right_view(root))
root = TreeNode(0, TreeNode(1, TreeNode(3)), TreeNode(2))
print(tree_right_view(root))

# time and space: O(n)