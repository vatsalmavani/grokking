# LC: https://leetcode.com/problems/missing-number/
# NC: https://youtu.be/WnPLSRLSANE
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743705616_30Unit

# iter and next functions explained: https://youtu.be/Dyu08G2l71c


def f(nums):
    s = set()
    for i in range(len(nums)+1):    # O(n)
        s.add(i)
    for i in nums:                  # O(n)
        s.remove(i)
    return int(next(iter(s)))       # O(1)

print(f([1,3,4,0]))
# O(n) time and O(n) space

'''
# gives an error in [0,1] since 2 is not in nums
def g(nums):
    nums.sort()
    for i in range(len(nums)):
        if nums[i] != i:
            return i
'''
# hence following code
def g(nums):
    nums.sort()
    if nums[-1] != len(nums):
        return len(nums)
    else:
        for i in range(len(nums)):
            if nums[i] != i:
                return i
# but sorting takes O(nlogn) time and O(n) space
# hence, use cyclic sort as it takes O(n) time and O(1) space

def h(nums):
    i, n = 0, len(nums)
    while i < n:
        # [0,2,4,1]
        correct_index = nums[i]
        if nums[i] < n and nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]  # swap
        else:
            i += 1
    # find the first number missing from its index, that will be our required number
    for i in range(n):
        if nums[i] != i:
            return i
    return n


# neetcode:
def f(nums):
    n = len(nums)
    return n*(n+1)//2 - sum(nums)