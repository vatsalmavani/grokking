# LC problem statement: https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
# mono queue explained (part 1): https://www.youtube.com/watch?v=J1rJ3IcwhKI
# mono queue part 2: https://www.youtube.com/watch?v=9hd8UFAYa1c
# watch part 2 from 9 mins, 15 secs if just want to know how monotonic queue works\
# watch part 1 & 2 both to understand why we need mono queue
# approach: https://www.youtube.com/watch?v=LDFZm4iB7tA
# this code copied from: https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/discuss/609708/Python-Clean-Monotonic-Queue-solution-with-detail-explanation-O(N)


# Sliding window minimum/maximum = monotonic queue.

# here, since we need to find max and min element in each window, we need monotonic queue

from collections import deque


def longestSubarray(nums, limit):
    incMonoQueue, decMonoQueue = deque(), deque()
    ans = 0
    l = 0

    for r in range(len(nums)):
        
        # add r to increasing monotonic queue if nums[r] is less than last element of the queue
        while incMonoQueue and nums[r] < nums[incMonoQueue[-1]]:    # note that in inc and dec mono queues, indices are sacved and not the actual nums' elements
            incMonoQueue.pop()
        incMonoQueue.append(r)

        # add r to decreasing monotonic queue if nums[r] is greater than last element of the queue
        while decMonoQueue and nums[r] > nums[decMonoQueue[-1]]:
            decMonoQueue.pop()
        decMonoQueue.append(r)

        while nums[decMonoQueue[0]] - nums[incMonoQueue[0]] > limit:
            l += 1
            if l > decMonoQueue[0]:
                decMonoQueue.popleft()
            if l > incMonoQueue[0]:
                incMonoQueue.popleft()
        
        ans = max(ans, r-l+1)
    
    return ans


# more intuitive solution:
###########################################################################


def f(nums, limit):
    l = 0
    maxlen = 0
    incq, decq = deque(), deque()
    for r in range(len(nums)):
        while incq and nums[r] < incq[-1]:
            incq.pop()
        incq.append(nums[r])

        while decq and nums[r] > decq[-1]:
            decq.pop()
        decq.append(nums[r])

        # while abs diff is > than limit, increase l. And remove elements from both queues which are no longer in window
        while decq[0] - incq[0] > limit:
            if decq[0] == nums[l]:
                decq.popleft()
            if incq[0] == nums[l]:
                incq.popleft()
            l += 1
        
        maxlen = max(maxlen, r-l+1)
    return maxlen

# this nums chosen to help you better understand the code in python tutor
nums = [4,4,2,1,5,6,3,7]; limit = 4
print(f(nums, limit))


nums = [8,2,4,7]; limit = 4
print(f(nums, limit))
nums = [10,1,2,4,7,2]; limit = 5
print(f(nums, limit))
nums = [4,2,2,2,4,4,2,2]; limit = 0
print(f(nums, limit))
print(f([5,5,5,4,3,6,2,1], 1))