# leetcode: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# neetcode: https://www.youtube.com/watch?v=DEJAZBq0FDA
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743424499_2Unit

# python implementation on first thought:

# def removeDuplicates1(arr) -> int:   # basically we have to return k (length of array after removing duplicates) and modify arr
#     for p in range(len(arr)):   # p = pointer
#         if p > 0 and arr[p] == arr[p-1]:
#             arr.remove(arr[p])
#     return len(arr)

# but this will give an index error since every time a duplicate is removed, array size decreases but range(len(arr)) in the for loop doesn't
# so we'll have to modify it accordingly

# try in python tutor if you don't get my point
# arr = [2, 3, 3, 3, 6, 9, 9]
# print(removeDuplicates1(arr))
# print(arr)

# def removeDuplicates2(arr):
#     for p in range(1, len(arr)):
#         if p >= len(arr):    # this len(arr) is calculated during each iteration as oppossed to the range(len(arr)) which is a range object - created once, not edited
#             break
#         if arr[p] == arr[p-1]:
#             arr.remove(arr[p])
#     return len(arr)

# arr = [2, 3, 3, 3, 6, 9, 9]
# print(removeDuplicates2(arr))
# print(arr)

# but here, the pointer keeps moving forward even after removing an element so it will give repeated elements
# no choice other than using two pointers

# for i in range(1,1):
#     print(i)
# this doesn't throw an error and nums > 1 in LC problem hence range(1, len(arr)) won't get executed of len(arr) = 1 and hence no error

def removeDuplicate(nums):
    l = 1
    for r in range(1, len(nums)):
        if nums[r] != nums[r-1]:
            nums[l] = nums[r]
            l += 1
    return l

# same code, my own implementation according to neetcode's logic
def f(nums):
    l,r = 1,1
    while r < len(nums) and l < len(nums):
        if nums[r] == nums[r-1]:
            r += 1
        else:
            nums[l] = nums[r]
            l += 1
            r += 1
    return nums

print(f([1,1,2,2,2,3,3,3,3,4]))