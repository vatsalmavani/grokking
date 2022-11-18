# LC: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# grokking (scroll down): https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743873257_48Unit

# note: maximum depth is also known as BST's height

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Instead of returning as soon as we find a leaf node, (like in finding min depth)
# we will keep traversing for all the levels,
# incrementing maximumDepth each time we complete a level

# basically, counting levels
def max_depth(root):
    if not root:
        return 0
    queue = deque([root])
    max_tree_depth = 0
    while queue:
        max_tree_depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return max_tree_depth

root = TreeNode(0, TreeNode(1, TreeNode(3)), TreeNode(2, TreeNode(4), TreeNode(5)))
print(max_depth(root))

# time & space: O(n)

def f(root):
    res = 0
    if not root: return res
    level = 0
    queue = deque([root])
    while queue:
        level += 1
        for _ in range(len(queue)):
            denode = queue.popleft()
            if not denode.left and not denode.right:
                res = level
            if denode.left:
                queue.append(denode.left)
            if denode.right:
                queue.append(denode.right)
    return res