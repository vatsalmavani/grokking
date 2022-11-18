# LC: https://leetcode.com/problems/container-with-most-water/
# neetcode: https://youtu.be/UuiTKBwPgAo

# brute force: O(N^2)
def maxWaterBruteForce(heights):
    maxWater = 0
    for l in range(len(heights)):
        for r in range(l+1, len(heights)):
            curWater = min(heights[l], heights[r])*(r-l)
            maxWater = max(curWater, maxWater)
    return maxWater

print(maxWaterBruteForce([1,8,6,2,5,4,8,3,7]))

# linear time solution: greedy method
def maxWater(height):
    maxWater = 0
    l,r = 0, len(height) - 1
    while l < r:
        curWater = min(height[l], height[r])*(r-l)
        maxWater = max(curWater, maxWater)

        if height[l] <= height[r]: l += 1
        else: r -= 1
    return maxWater

print(maxWater([1,8,6,2,5,4,8,3,7]))

### OR ###

def water(height):
    n = len(height)
    l,r = 0, n-1
    maxWater = 0
    while l < r:
        if height[l] <= height[r]:
            maxWater = max(maxWater, height[l]*(r-l))
            l += 1
        else:
            maxWater = max(maxWater, height[r]*(r-l))
            r -= 1
    return maxWater

def f(nums):
    l,r = 0, len(nums)-1
    maxwater = (r-l)*min(nums[l], nums[r])
    while l < r:
        if nums[l] < nums[r]:
            l += 1
        else:
            r -= 1
        maxwater = max(maxwater, (r-l)*min(nums[l], nums[r]))
    return maxwater