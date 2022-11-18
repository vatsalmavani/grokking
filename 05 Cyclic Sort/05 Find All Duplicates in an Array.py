# LC: https://leetcode.com/problems/find-all-duplicates-in-an-array/
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743734011_33Unit

def cyclic_sort(nums):
    # sort in O(n) time, O(1) space
    i = 0
    while i < len(nums):
        correct_index = nums[i] - 1
        if nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1
    # check if duplicate exists
    # this gives error. see in python tutor
    '''
    res = []
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            res.append(nums[i])
    return res
    '''
    res = []
    for i in range(len(nums)):
        if nums[i] != i+1:
            res.append(nums[i])
    return res

# try to apply this input to the code which we "stringed out"
print(cyclic_sort([4,3,2,7,8,2,3,1]))