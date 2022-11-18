# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743880609_49Unit

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def f(root, node):
    queue = deque([root])
    prevnode = None
    while queue:
        denode = queue.popleft()
        if node == prevnode:
            return denode.val
        if denode.left:
            queue.append(denode.left)
        if denode.right:
            queue.append(denode.right)
        prevnode = denode

def find_successor(root, node):
    queue = deque([root])
    while queue:
        deNode = queue.popleft()
        if deNode.left:
            queue.append(deNode.left)
        if deNode.right:
            queue.append(deNode.right)
        
        if not queue:
            return None
        # this is wrong since comparing two objects with == will always return False
        # if deNode == node:
        #     return queue.popleft()
        if deNode == node:
            tmp = queue.popleft()
            return tmp.val

root = TreeNode(0)
one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
five = TreeNode(5)
root.left = one
root.right = two
one.left = three
two.left = four
two.right = five
print(find_successor(root, root.right))

# time & space: O(n)