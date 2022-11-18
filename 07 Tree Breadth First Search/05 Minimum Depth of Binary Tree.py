# LC: https://leetcode.com/problems/minimum-depth-of-binary-tree/
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743873257_48Unit

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def min_depth(root):
    if not root:
        return 0
    queue = deque([root])
    level = 0
    while queue:
        level += 1
        for _ in range(len(queue)):
            deNode = queue.popleft()
            if not deNode.left and not deNode.right:
                return level
            if deNode.left:
                queue.append(deNode.left)
            if deNode.right:
                queue.append(deNode.right)

root = TreeNode(0, TreeNode(1, TreeNode(3)), TreeNode(2, TreeNode(4), TreeNode(5)))
print(min_depth(root))

# time & space: O(n)