# LC: https://leetcode.com/problems/3sum/
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743445291_4Unit

# note: brute force = O(n^3) time complexity while solving with 2 pointers = O(n^2) TC

def threeSum(nums):
    res = []
    nums.sort()

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        l, r = i+1, len(nums) - 1
        while l < r:
            _3sum_ = nums[i] + nums[l] + nums[r]

            if _3sum_ > 0:
                r -= 1
            elif _3sum_ < 0:
                l += 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                # see grokking and neetcode to understand why these two while loops are necessary
                # OR remove these two loops and see in python tutor with nums = [-2,-2,0,0,2,2]
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while l < r and nums[r] == nums[r+1]:
                    r -= 1
            
    return res

nums = [-2,-2,0,0,2,2]
print(threeSum(nums))