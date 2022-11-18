# LC: https://leetcode.com/problems/sliding-window-maximum/

# brute force

from collections import deque


def slidingWindowMax(nums, k):
    res = []
    for l in range(len(nums) - k + 1):
        windowMax = float('-inf')
        for i in range(l, l+k):
            windowMax = max(windowMax, nums[i])
        res.append(windowMax)
    return res

nums = [1,3,-1,-3,5,3,6,7]; k = 3
print(slidingWindowMax(nums, k))

# this is brute force bcoz each time outer loop runs, inner loop calculates same thing again (except for the first and last elements)
# time complexity is O(k*(n-k))
# if k = n/2 then time complexity becomes O(n^2/4) = O(n^2)

# sliding window + mono queue (min/max in sliding window = mono queue)

def slidingWindowMax(nums, k):
    # since given that 1 <= k <= nums, no edge case of k > nums.length
    decMonoQueue = deque()
    res = []
    l = 0

    for r in range(len(nums)):
        while decMonoQueue and nums[r] > nums[decMonoQueue[-1]]:
            decMonoQueue.pop()
        decMonoQueue.append(r)

        while r-l+1 > k:
            l += 1
            if l > decMonoQueue[0]:
                decMonoQueue.popleft()

        if r-l+1 == k:
            res.append(nums[decMonoQueue[0]])
    
    return res