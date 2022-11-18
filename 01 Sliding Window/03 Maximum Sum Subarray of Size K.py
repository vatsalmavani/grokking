# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1627871358579_1Unit

arr1 = [2, 1, 5, 1, 3, 2]
k1 = 3

arr2 = [2, 3, 4, 1, 5]
k2 = 2

def max_sum_sub(arr, k):
    window_sum = window_start = 0
    result = float('-inf')
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= k-1:
            result = max(result, window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    return result

print(max_sum_sub(arr1, k1))
print(max_sum_sub(arr2, k2))

# time complexity = O(N); N = no of elements in the array
# space comp = O(1)

# easier way: since all numbers are +ve, this code will work just fine

def maxsum(arr, k):
    max_sum, window_sum = 0,0
    l = 0
    for r in range(len(arr)):
        window_sum += arr[r]
        while r-l+1 > k:     # while window size is greater than k, decrease l
            window_sum -= arr[l]
            l += 1
        # max_sum is out of the while loop/if statement bcoz:
        # all numbers are positive so until window size is max, max_sum is not maximum. new positive numbers are yet to come
        max_sum = max(max_sum, window_sum)
    return max_sum

print(maxsum(arr1, k1))
print(maxsum(arr2, k2))