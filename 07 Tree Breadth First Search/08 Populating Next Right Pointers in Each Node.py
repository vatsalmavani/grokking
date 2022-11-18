# LC: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743890075_50Unit

# in LC, it says the tree is perfect BST but in grokking, it is not speciied
# so we will not assume that the BST is perfect


from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = None
    
def connect_level_order_siblings(root):
    if not root:
        return
    
    queue = deque([root])
    while queue:
        prevNode = None
        for _ in range(len(queue)):
            currNode = queue.popleft()
            if prevNode:
                prevNode.next = currNode
            prevNode = currNode
            
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)
    return root


root = TreeNode(0, TreeNode(1, TreeNode(3)), TreeNode(2, TreeNode(4), TreeNode(5)))
connect_level_order_siblings(root)

# time & space: O(n)