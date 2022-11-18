# leetcode: https://leetcode.com/problems/minimum-size-subarray-sum/

def greater_or_equal_sum_subarray(arr, s):
    window_sum = window_start = 0
    min_length = float('inf')
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    if min_length == float('inf'):  # this condn is necessary for edge cases where the window_sum will always be less than s
        return 0
    return min_length

arr1 = [2, 1, 5, 2, 3, 2]; s1=7
arr2 = [2, 1, 5, 2, 8]; s2=7
arr3 = [3, 4, 1, 1, 6]; s3=8
arr4 = [3, 4, 1, 1, 6]; s4=80

print(greater_or_equal_sum_subarray(arr1,s1))
print(greater_or_equal_sum_subarray(arr2,s2))
print(greater_or_equal_sum_subarray(arr3,s3))
print(greater_or_equal_sum_subarray(arr4,s4))