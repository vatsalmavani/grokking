# LC: https://leetcode.com/problems/subsets/
# NC (backtracking): https://youtu.be/REOH22Xwdkk
# fraz (backtracking): https://youtu.be/0N3RCWa8jFM?t=646
# grokking (bfs solution): https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628744042826_67Unit
# Aditya verma (dfs solution): https://youtu.be/Yg5a2FxU4Fo

# bfs solution
def find_subsets(nums):
    subsets = []
    subsets.append([])
    for currentNumber in nums:
        n = len(subsets)
        for i in range(n):  # O(2^n) (see below why)
            # here, list(subset) is necessary since if you wrote only set1 = subsets[i], it would be a reference and not a different object/list
            set1 = list(subsets[i]) # O(n)
            set1.append(currentNumber)
            subsets.append(set1)
    return subsets

'''
total subsets were 1 at first, became 2 WHEN CURRENTNUMBER IS ADDED, became 4 and so on
i ranges from 0 to 1, 0 to 2, 0 to 4...
ie. 1 + 2 + 4 + ... + 2^n = 2^(n+1) - 1 = O(2^n)
Note that O(2^n) is combined complexity of the two for loops

in grokking's words:
Since, in each step, the number of subsets doubles as we add each element to all the existing subsets,
therefore, we will have a total of O(2^N) subsets, where 'N' is the total number of elements in the input set.
And since we construct a new subset from an existing set, therefore, the time complexity of the above algorithm will be O(N*2^N)

All the additional space used by our algorithm is for the output list.
Since we will have a total of O(2^N) subsets, and each subset can take up to O(N) space, therefore, the space complexity of our algorithm will be O(N*2^N)
'''

# dfs solution
def subsets(nums):
    def dfs(ip, op, res): # input, output
        if len(ip) == 0:
            res.append(op)
            return
        dfs(ip[1:], op, res)
        dfs(ip[1:], op + [ip[0]], res)
        return res
    return dfs(nums, [], [])

def subsets_backtrack(nums):
    res = []
    subset = []
    def dfs(idx):
        if idx == len(nums):
            res.append(subset.copy()) # makes a copy not doesnt refer to the object. similar to what we did in bfs - list(subset) - this works too
            return
        
        subset.append(nums[idx])
        dfs(idx + 1)
        subset.pop()
        dfs(idx + 1)

        return res
    return dfs(0)

print(subsets_backtrack([1,2,3]))

# bfs intuitive
# https://leetcode.com/problems/subsets/discuss/277064/bfs-to-generate-subset
# Imagine sub-set generation as an implicit binary tree, where the node is a set A, and its 2 children are A + [x] and A + [].
# Do a level order BFS, and stop at level == len(nums)
def subsets_bfs(nums):
    from collections import deque
    queue = deque([[]])
    i = 0
    while queue and i < len(nums):
        for _ in range(len(queue)):
            deNum = queue.popleft()
            queue.append(deNum) # no need of deNum[:] ie. to create a new list since this list won't be used in future
            queue.append(deNum + [nums[i]])
        i += 1
    return list(queue)
# note that here repeated work is done - popleft and append the same subset

# intuitive dfs
# https://stackoverflow.com/questions/46780587/enumerate-subsets-with-dfs
def subsets_dfs(nums):
    res = []
    def dfs(nums, res, cur, pos):
        for i in range(pos, len(nums)):
            res.append(cur + [nums[i]])
            dfs(nums, res, cur + [nums[i]], i + 1)
    dfs(nums, res, [], 0)
    return res
print(subsets_dfs([1,2,3]))