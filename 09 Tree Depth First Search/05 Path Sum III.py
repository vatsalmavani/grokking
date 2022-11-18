# LC: https://leetcode.com/problems/path-sum-iii/
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743955693_58Unit
# do '01 subarray sum equals k' in the prefix sum to understand the second solution

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# MY solution:

def f(root, target):
    presum = 0
    res = 0
    h = {0:1}
    def dfs(root):
        if not root:
            return
        nonlocal presum, res, target
        presum += root.val
        if presum - target in h:
            res += h[presum - target]
        h[presum] = h.get(presum, 0) + 1
        dfs(root.left)
        dfs(root.right)
        h[presum] -= 1
        presum -= root.val
        '''
        my mistake: this is not how backtracking works (see in python tutor why)
        it will give you an error: noneType has no attribute 'val'

        dfs(root.left)
        h[presum] -= 1
        presum -= root.left.val
        dfs(root.right)
        h[presum] -= 1
        presum -= root.right.val
        '''
    dfs(root)
    return res


# solution: https://youtu.be/6jYxwdwjwKg

def f(root, targetSum):
    res = 0
    h = {0:1}
    def dfs(root, ps):  # previous sum
        if not root:
            return
        nonlocal res
        cs = ps + root.val  # current sum
        if cs - targetSum in h:
            res += h[cs - targetSum]
        h[cs] = h.get(cs, 0) + 1
        dfs(root.left, cs)
        dfs(root.right, cs)
        h[cs] -= 1
        return res
    return dfs(root, 0) if root else 0

root = TreeNode(10)
root.left = one = TreeNode(5)
root.right = two = TreeNode(-3)
one.left = three = TreeNode(3)
one.right = four = TreeNode(2)
two.right = TreeNode(11)
three.left = TreeNode(3)
three.right = TreeNode(-2)
four.right = TreeNode(1)
f(root, 8)


# codebix solution: https://youtu.be/yyZA4v0x16w

def find_path_sum_brute_force(root, targetSum):
    total = 0
    def left_pointer_fixed(root, currentSum, targetSum):
        if not root: return

        nonlocal total
        currentSum += root.val
        if currentSum == targetSum:
            total += 1
        left_pointer_fixed(root.left, currentSum, targetSum)
        left_pointer_fixed(root.right, currentSum, targetSum)

    def left_pointer_moves(root, targetSum):
        if not root: return 0

        left_pointer_fixed(root, 0, targetSum)
        left_pointer_moves(root.left, targetSum)
        left_pointer_moves(root.right, targetSum)

        return total
    
    return left_pointer_moves(root, targetSum)

root = TreeNode(0, TreeNode(1, TreeNode(3)), TreeNode(2, TreeNode(4), TreeNode(5)))
print(find_path_sum_brute_force(root, 6))
# time: O(n^2)
# note: modifying global or nonlocal variable requires us to declare that
# accessing a global/nonlocal variable doesn't
# that's why when doing total += 1, we declared nonlocal total while return total didn't require us to declare that

# do the O(n) time solution once you understand prefix sum

def find_path_sum_using_preix_sum(root, targetSum):
    total = 0
    def path_sum(root, targetSum):
        if not root:
            return 0
        prefix_sum_freq = {0:1}
        find_path_sum_2(root, targetSum, 0, prefix_sum_freq)
        return total
    
    def find_path_sum_2(root, targetSum, currentSum, prefix_sum_freq):
        if not root:
            return
        nonlocal total
        currentSum += root.val
        if currentSum - targetSum in prefix_sum_freq:
            total += prefix_sum_freq[currentSum - targetSum]
        prefix_sum_freq[currentSum] = prefix_sum_freq.get(currentSum, 0) + 1
        find_path_sum_2(root.left, targetSum, currentSum, prefix_sum_freq)
        find_path_sum_2(root.right, targetSum, currentSum, prefix_sum_freq)
        prefix_sum_freq[currentSum] -= 1
    
    return path_sum(root, targetSum)

root = TreeNode(0, TreeNode(1, TreeNode(3)), TreeNode(2, TreeNode(4), TreeNode(5)))
print(find_path_sum_using_preix_sum(root, 6))
# time: O(n)
# space: O(n)