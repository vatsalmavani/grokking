# LC: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743852073_45Unit

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_reverse(root):
    res = deque()
    if not root:
        return list(res)
    queue = deque([root])
    while queue:
        curr_list = []
        for _ in range(len(queue)):
            curr_node = queue.popleft()
            curr_list.append(curr_node.val)
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        res.appendleft(curr_list)
    return list(res)

# time & space: O(n)
# list(res) time and space: O(n)

root = TreeNode(0, TreeNode(1, TreeNode(3)), TreeNode(2, TreeNode(4), TreeNode(5)))
print(level_order_reverse(root))
root = None
print(level_order_reverse(root))
root = TreeNode(1)
print(level_order_reverse(root))