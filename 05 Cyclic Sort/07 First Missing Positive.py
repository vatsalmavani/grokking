# LC: https://leetcode.com/problems/first-missing-positive/
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743750267_35Unit

def first_missing_positive(nums):
    i = 0
    while i < len(nums):
        correct_index = nums[i] - 1 # correct index
        if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1
    return len(nums) + 1