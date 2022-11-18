# LC: https://leetcode.com/problems/4sum/
# neetcode (recursive solution to avoid so many loops): https://www.youtube.com/watch?v=EYeR-_1NRlQ

# 4sum = basically 3sum with extra for loop

# kSum - recursive
def fourSum(nums, target):
    nums.sort()
    res, quad = [], []

    def kSum(k, start, target):
        if k != 2:
            for i in range(start, len(nums) - k + 1):
                if i > start and nums[i] == nums[i-1]:
                    continue
                quad.append(nums[i])
                kSum(k-1, i+1, target - nums[i])
                quad.pop()
            return
        
        # base case: k = 2
        l,r = start, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                res.append(quad + [nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while l < r and nums[r] == nums[r+1]:
                    r -= 1
    
    kSum(4, 0, target)
    return res

print(fourSum([2,2,2,2,2], 8))

# O(n^3) time
# O(n) space



# 4Sum iterative
def foursum(nums, target):
    nums.sort()
    res = []
    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, len(nums) - 2):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            l, r = j+1, len(nums)-1
            while l < r:
                cur_sum = nums[i] + nums[j] + nums[l] + nums[r]
                if cur_sum < target:
                    l += 1
                elif cur_sum > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
    return res

nums = [4, 1, 2, -1, 1, -3]; target=1
print(foursum(nums, target))

# time: O(n^3)
# space: O(n) used for sorting