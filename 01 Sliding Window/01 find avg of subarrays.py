'''
Q: find the avg of every window of size k
https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1627871350324_0Unit
'''

def find_average_of_subarrays(k, arr):  # k = window size
    result = []
    window_sum, window_start = 0,0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= k - 1:
            result.append(window_sum/k)
            window_sum -= arr[window_start]
            window_start += 1
    return result

arr = [1,2,3,4,5,6,7,8,9]
print(find_average_of_subarrays(5,arr))

# easier implementation:

def avg(arr, k):
    window_sum = 0
    l = 0
    res = []
    for r in range(len(arr)):
        window_sum += arr[r]
        if r-l+1 > k:
            window_sum -= arr[l]
            l += 1
        if r-l+1 == k:
            res.append(window_sum/k)
    return res

print(avg(arr, 3))