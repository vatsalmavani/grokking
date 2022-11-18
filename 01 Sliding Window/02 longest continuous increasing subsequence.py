"""
Q: find the length of longest continuous, increasing subsequence
LC: https://leetcode.com/problems/longest-continuous-increasing-subsequence/

https://www.youtube.com/watch?v=W9Mi4r4lmkI
"""

arr = [1,2,3,2,3,4,5,3,2,8]

def long_cont_increasing_sub(arr):
    result = window_start = 0
    for window_end in range(len(arr)):
        if window_end > 0 and arr[window_end-1] >= arr[window_end]:
            window_start = window_end
        result = max(result, window_end - window_start + 1)
    return result

print(long_cont_increasing_sub(arr))