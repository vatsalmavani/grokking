# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743744011_34Unit

def f(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return [nums[i], i+1]
    return [-1, -1]

# time: O(n)
# space: O(1)

print(f([3, 1, 2, 5, 2]))
print(f([3, 1, 2, 3, 6, 4]))