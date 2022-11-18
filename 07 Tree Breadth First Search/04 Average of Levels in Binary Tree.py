# LC: https://leetcode.com/problems/average-of-levels-in-binary-tree/
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743864804_47Unit

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def avg_of_levels(root):
    res = []
    if not root:
        return res
    queue = deque([root])
    while queue:
        node_count = len(queue)
        level_sum = 0
        for _ in range(len(queue)):
            deNode = queue.popleft()
            level_sum += deNode.val
            if deNode.left:
                queue.append(deNode.left)
            if deNode.right:
                queue.append(deNode.right)
        res.append(level_sum/node_count)
    return res

root = TreeNode(0, TreeNode(1, TreeNode(3)), TreeNode(2, TreeNode(4), TreeNode(5)))
print(avg_of_levels(root))

def max_of_levels(root):
    res = []
    if not root:
        return res
    queue = deque([root])
    while queue:
        level_max = 0
        for _ in range(len(queue)):
            deNode = queue.popleft()
            level_max = max(level_max, deNode.val)
            if deNode.left:
                queue.append(deNode.left)
            if deNode.right:
                queue.append(deNode.right)
        res.append(level_max)
    return res

root = TreeNode(0, TreeNode(1, TreeNode(3)), TreeNode(2, TreeNode(4), TreeNode(5)))
print(max_of_levels(root))

# time & space: O(n)