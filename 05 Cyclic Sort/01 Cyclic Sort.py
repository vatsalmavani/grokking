# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743698633_29Unit
# explained: https://youtu.be/YvksaZhYYAk

# sort an array in O(n) time, O(1) space if all the elements belong to range(1,n)


def f(nums):
    i = 0
    while i < len(nums):
        # the valid position of any number nums[i] is nums[i] - 1
        # since range is from 1 to n
        # so, sorted array looks like this: [1,2,3,4,5]
        # as you can see, 1 @ index 0; 2 @ index 1 etc.
        correct_index = nums[i] - 1
        if nums[i] != nums[correct_index]:  # i is not the correct index
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1
    return nums

print(f([3,2,1,4,5]))


# to understand why we NEED another variable - correct_index, see this in python tutor:
# basically since we modified nums[i] already, it affects in nums[i] = nums[nums[i] - 1]

# note that nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i] and the following code are exactly the same
# temp = nums[i]
# nums[i] = nums[nums[i] - 1]
# nums[nums[i] - 1] = temp
def f(nums):
    i = 0
    while i < len(nums):
        if nums[i] != nums[nums[i] - 1]:
            temp = nums[i]
            nums[i] = nums[nums[i] - 1]
            # here, since nums[i] is changed, the following nums[i] in nums[nums[i]-1] is not the same as previous line's nums[i]
            nums[nums[i] - 1] = temp
        else:
            i += 1
    return nums

print(f([3, 1, 5, 4, 2]))