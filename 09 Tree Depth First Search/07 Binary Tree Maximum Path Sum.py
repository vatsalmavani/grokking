# LC: https://leetcode.com/problems/binary-tree-maximum-path-sum/
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743967658_60Unit
# NC (to understand this code): https://youtu.be/Hr5cWUld4vU

def find_max_path_sum(root):
    res = root.val
    def dfs(root):
        if not root:
            return 0
        
        leftMax = dfs(root.left)
        rightMax = dfs(root.right)
        leftMax = max(leftMax, 0)
        rightMax = max(rightMax, 0)

        nonlocal res
        res = max(res, root.val + leftMax + rightMax)

        return root.val + max(leftMax, rightMax)
    
    dfs(root)
    return res