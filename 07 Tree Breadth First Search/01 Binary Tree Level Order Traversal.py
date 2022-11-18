# LC: https://leetcode.com/problems/binary-tree-level-order-traversal/
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743844952_44Unit

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    res = []
    if not root:
        return res
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
        res.append(curr_list)
    return res

# time complexity: O(n) since we traverse each node
# space comp = O(n) since at the last level, we might have N/2 nodes in the queue

root = TreeNode(0, TreeNode(1, TreeNode(3)), TreeNode(2, TreeNode(4), TreeNode(5)))
print(level_order(root))
root = None
print(level_order(root))
root = TreeNode(1)
print(level_order(root))