# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743754602_36Unit
# LC (different question): https://leetcode.com/problems/kth-missing-positive-number/

# this is a stupid question bcoz using set and 'in' takes O(n + k) time and O(n) space
# this grokking implementation takes O(n + k) time and O(k) space

def missing_nums(nums, k):
    i = 0
    while i < len(nums):
        correct_index = nums[i] - 1 # correct index
        if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1
    # find missing numbers from the array
    missing_numbers = []
    extra_nums = set()
    for i in range(len(nums)):
        if len(missing_numbers) < k:
            if nums[i] != i + 1:
                missing_numbers.append(i+1)
                extra_nums.add(nums[i])
    # find missing numbers from outside the array range
    i = 1
    while len(missing_numbers) < k:
        candidate_num = i + len(nums)
        if candidate_num not in extra_nums:
            missing_numbers.append(candidate_num)
        i += 1
    return missing_numbers


##### my 'smart' approach #####

def f(nums, k):
    # this is useless code
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if 0 < nums[i] < len(nums) and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    # useless code till here
    i = 1
    res = []
    while len(res) < k:
        if i not in nums:
            res.append(i)
        i += 1
    return res

# FUCKING DIDN'T HAVE TO SORT IF YOU'RE USING 'IN' TO CHECK
# 'in' 'funcn' of list takes O(n) time
# so total time is O(k*n) (O(n) for each execution of while loop)
# space is O(1)
# we can reduce time to O(k) by converting nums to set: nums = set(nums)
# since 'in' 'funcn' takes O(1) to look up
# but space increases to O(n)