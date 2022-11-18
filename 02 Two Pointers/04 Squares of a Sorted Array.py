# LC: https://leetcode.com/problems/squares-of-a-sorted-array/
# grokking (this code): https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743435284_3Unit

# brute force

# def squareSorted(nums):     # O(nlogn) time and O(1) space
#     for i in range(len(nums)):  # ---> O(n)
#         nums[i] = nums[i]**2
#     nums.sort()     # ---------------> O(nlogn)
#     return nums

# nums = [-2, -1, 0, 2, 3]
# print(squareSorted(nums))

# solve in O(n) time complexity

def squareSorted(nums):
    n = len(nums)
    sortedSquares = [0]*n
    highestSquareIndex = n - 1
    left, right = 0, n-1
    while left <= right:
        lsquare = nums[left]**2
        rsquare = nums[right]**2
        if lsquare > rsquare:
            sortedSquares[highestSquareIndex] = lsquare
            left += 1
        else:
            sortedSquares[highestSquareIndex] = rsquare
            right -= 1
        highestSquareIndex -= 1
    return sortedSquares

nums = [-2, -1, 0, 2, 3]
print(squareSorted(nums))