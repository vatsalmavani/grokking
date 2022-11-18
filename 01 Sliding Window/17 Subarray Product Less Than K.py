# grokking (this code): https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743479436_7Unit
# LC: https://leetcode.com/problems/subarray-product-less-than-k/

# this problem is in two pointers section in grokking but is actually sliding window problem

from collections import deque


def find_subarrays(arr, target):
    result = []
    product = 1
    left = 0
    for right in range(len(arr)):   # O(n)
        product *= arr[right]
        while (product >= target and left <= right):
            product /= arr[left]
            left += 1
        # since the product of all numbers from left to right is less than the target 
        # therefore, all subarrays from left to right will have a product less than the 
        # target too; to avoid duplicates, we will start with a subarray containing only 
        # arr[right] and then extend it
        temp_list = deque()
        for i in range(right, left-1, -1):  # O(n) in worst case
            temp_list.appendleft(arr[i])
            result.append(list(temp_list))  # O(n) time to convert deque to list. So, total time of this for loop is O(n^2)
    return result

# O(n^3) time complexity


def main():
    print(find_subarrays([2, 5, 3, 100, 15], 300))
    print(find_subarrays([8, 2, 6, 5], 50))
    print(find_subarrays([1,2,3], 0))

main()

def smaller_product(nums, k):
    l, prod, count = 0,1,0
    for r in range(len(nums)):
        prod *= nums[r]
        while prod >= k and l <= r:     # with nums = [1,2,3] and k = 0, you can see in python tutor why l <= r is necessary
            prod /= nums[l]
            l += 1
        count += r-l+1  # to understand why r-l+1, watch this video: https://www.youtube.com/watch?v=CBY4mis_HF4 or read the comments below
    return count

# O(n) time and O(1) space
# The right pointer goes through the entire array: O(n)
# The left pointer (at most) goes through the entire array: O(n)


print(smaller_product([2, 5, 3, 100, 15], 30))
print(smaller_product([8, 2, 6, 5], 50))
print(smaller_product([1,2,3], 0))

'''
say list is [1,2,3,4] and k is very large. So we don't need to take that into consideration
so our subarrays with product less than k will be:
[1], [2], [3], [4]  --> 4
[1,2], [2,3], [3,4] --> 3
[1,2,3], [2,3,4]    --> 2
[1,2,3,4]           --> 1

total = 4+3+2+1 = 10

the reason for count += r-l+1 :
window increases incrementally. So first window size will be 1 then 2 then 3 then 4
so basically we are doing 1+2+3+4 = 10
'''

def smaller_product(nums, k):
    l, prod, count = 0,1,0
    for r in range(len(nums)):
        prod *= nums[r]
        while prod >= k and l <= r:
            prod /= nums[l]
            l += 1
        if prod < k:
            count += r-l+1
    return count