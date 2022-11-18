# LC premium: 1430
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743947562_57Unit

# IMPORTANT: draw a recursion tree to understand THEN visualise in python tutor

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# MY approach: use sq = deque(sq); denode = sq.popleft() but it will have many edge cases
    
def find_path(root, sequence):
    if not root:
        return len(sequence) == 0

    def dfs(root, sequence, sqIndex):   # sq = sequence index
        if not root:
            return False
        if sqIndex >= len(sequence) or root.val != sequence[sqIndex]:
            return False
        if not root.left and not root.right and sqIndex == len(sequence) - 1: # root.val == sequence[sqIndex] is implicit
            return True
        return dfs(root.left, sequence, sqIndex + 1) or dfs(root.right, sequence, sqIndex + 1)
        
    return dfs(root, sequence, 0)

root = TreeNode(0, TreeNode(1, TreeNode(3)), TreeNode(2, TreeNode(4), TreeNode(5)))
print(find_path(root, [0,2,4]))
print(find_path(root, [0,2,4,3]))