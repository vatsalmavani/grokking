# LC: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743859019_46Unit

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# see what's wrong in this code
def zigzag_level_order(root):
    res = []
    if not root:
        return res
    queue = deque([root])
    left_to_right = True
    while queue:
        curlist = deque()
        for _ in range(len(queue)):
            node = queue.popleft()
            if left_to_right:
                curlist.append(node.val)
            else:
                curlist.appendleft(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(list(curlist))
        left_to_right = not left_to_right
    return res


root = TreeNode(0, TreeNode(1, TreeNode(3)), TreeNode(2, TreeNode(4), TreeNode(5)))
print(zigzag_level_order(root))

# time & space: O(n)