# leetcode: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743404181_0Unit
# grokking code: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743417172_1Unit

# IMP note: this problem is different from Leetcode's two sum problem
# input array is sorted in this problem. That's why we can use two pointers method
# in two sum, input array is not necessarily sorted so cant use two pointers


# this code works but look at it. IT"S MESSY
# this is the code I came up with immediately after studying sliding window
# the pointed out areas with '<--' are 'sliding window mindset'

# def arrIndex(arr, target):
#     l = 0   # left pointer
#     r = len(arr) - 1    # right pointer
#     sum_ = arr[l] + arr[r]  # <--
#     if sum_ == target:
#         return [l,r]
#     while sum_ != target:
#         if sum_ > target:
#             # decrease right pointer to decrease sum_
#             sum_ -= arr[r]  # <--
#             r -= 1
#             sum_ += arr[r]  # <--
#         elif sum_ < target:
#             # move left pointer to increase sum_
#             sum_ -= arr[l]  # <--
#             l += 1
#             sum_ += arr[l]  # <--
#     if sum_ == target:
#         return [l,r]
#     return [-1,-1]

# print(arrIndex([1, 2, 3, 4, 6], 6))
# print(arrIndex([2, 5, 9, 11], 11))

############################################################################

def arrIndex(arr, target):
    l, r = 0, len(arr) - 1
    while l < r:
        current_sum = arr[l] + arr[r]
        if current_sum == target:
            return [l,r]
        if current_sum > target:
            r -= 1
        if current_sum < target:
            l += 1
    return [-1,-1]