# LC: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
# concept from: https://www.youtube.com/watch?v=K0NgGYEAkA4
# code from: https://www.youtube.com/watch?v=j5zif7Gzg5Q


# google: 'when to use monotonic queue'
# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/204290/Monotonic-Queue-Summary


from collections import deque


def minSubarrayLen(target, nums):
    queue = deque()
    queue.append([0,0])
    window_sum = 0
    res = float('inf')

    for i, num in enumerate(nums):
        window_sum += num
        while queue and window_sum - queue[0][1] >= target:
            res = min(res, i - queue[0][0] + 1)
            queue.popleft()
        while queue and window_sum < queue[-1][0]:
            queue.pop()
        queue.append([i+1, window_sum])
    
    if res < float('inf'): return res
    return -1