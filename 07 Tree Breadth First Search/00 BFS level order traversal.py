from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order2(root):
    queue = deque([root])
    while queue:
        for _ in range(len(queue)):
            curr_node = queue.popleft()
            print(curr_node.val, end=' ')
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)

root = TreeNode(0, TreeNode(1, TreeNode(3)), TreeNode(2, TreeNode(4), TreeNode(5)))
level_order2(root)

print()

def level_order(root):
    queue = deque([root])
    while queue:
        curr_node = queue.popleft()
        print(curr_node.val, end=' ')
        if curr_node.left:
            queue.append(curr_node.left)
        if curr_node.right:
            queue.append(curr_node.right)

root = TreeNode(0, TreeNode(1, TreeNode(3)), TreeNode(2, TreeNode(4), TreeNode(5)))
level_order(root)