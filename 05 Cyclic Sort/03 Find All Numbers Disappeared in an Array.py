# LC: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# NC: https://youtu.be/8i-f24YFWC4
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743711992_31Unit

# neetcode has two different approaches as well

def f(nums):
    i = 0
    while i < len(nums):
        correct_index = nums[i] - 1
        if nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1
    res = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            res.append(i + 1)
    return res