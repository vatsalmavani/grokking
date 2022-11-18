# LC: https://leetcode.com/problems/subsets-ii/
# grokking (also see this code): https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628744050595_68Unit
# NC: https://youtu.be/Vn2v6ajA7U0

# neetcode: backtracking
def subsets(nums):
    nums.sort()
    res = []
    subset = []
    def dfs(idx):
        if idx == len(nums):
            res.append(subset.copy())
            return
        
        # all subsets that include nums[i]
        subset.append(nums[idx])
        dfs(idx + 1)
        subset.pop()

        # all subsets that don't include nums[i]
        while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
            idx += 1
        dfs(idx + 1)

    dfs(0)
    return res

print(subsets([1,2,2]))

# grokking: bfs (read the grokking article to understand)
def find_subsets(nums):
    nums.sort()
    subsets = []
    subsets.append([])
    startIndex, endIndex = 0, 0
    for i in range(len(nums)):
        startIndex = 0
        if i > 0 and nums[i] == nums[i-1]:
            startIndex = endIndex + 1
        endIndex = len(subsets) - 1
        for j in range(startIndex, endIndex + 1):
            set1 = list(subsets[j])
            set1.append(nums[i])
            subsets.append(set1)
    return subsets

print(find_subsets([1,2,2,3]))

def subsets_dfs(nums):
    res = []
    def dfs(nums, res, cur, pos):
        res.append(cur)
        for i in range(pos, len(nums)):
            if i > pos and nums[i] == nums[i-1]:
                continue
            dfs(nums, res, cur + [nums[i]], i + 1)
    dfs(nums, res, [], 0)
    return res
print(subsets_dfs([1,2,2,3]))