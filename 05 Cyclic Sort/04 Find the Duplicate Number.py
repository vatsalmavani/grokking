# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743725641_32Unit

# find the only duplicate number in an array in O(n) time, O(1) space
# you CAN modify input array

def brute_force(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return nums[i]

# note: cyclic sort is not like a normal sort. it doesn't work when there are duplicate values
# so this approach, which we used in the nums.sort() method, can't be used
# correct ans is purely accidental
# (see the next problem for an example)
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
    for i in range(len(nums)):
        if nums[i] != i+1:
            return nums[i]
    
def confusing_grokking(nums):
    i = 0
    while i < len(nums):
        if nums[i] != i + 1:
            correct_index = nums[i] - 1
            if nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]  # swap
            else:  # we have found the duplicate
                return nums[i]
        else:   # nums[i] is in its correct position
            i += 1
    return -1

print(brute_force([2,4,3,1,5,5]))
print(cyclic_sort([2,4,3,1,5,4]))
print(confusing_grokking([2,4,3,3,1]))