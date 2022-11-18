# LC: https://leetcode.com/problems/subarray-sum-equals-k/

# to understand the solution, read the LC solution first or understand the comments in the function
# then watch the video
# Then to understand res+=, read the reddit thread
# LC discussion solution: https://leetcode.com/problems/subarray-sum-equals-k/discuss/1759909/C%2B%2Bor-Full-explained-every-step-w-Dry-run-or-O(n2)-greater-O(n)-or-Two-approaches
# codebix solution (this code): https://youtu.be/MHocw0bP1rA
# reddit thread: https://www.reddit.com/r/leetcode/comments/y7m1ep/subarray_sum_equals_k/

def subarray_sum_equals_k(nums, k):
    # calculate prefix sum
    # if there exists prefixSum[i] - prefixSum[j] == k: (i > j)
        # then this means that there is a subarray whose sum is k
    # so if prefixSum[i] - k (i.e. prefixSum[j]) exists in the hashmap, this means that there is a subarray with sum equals k
    # the subarray is from index j+1 to i
    summ = res = 0
    prefixSum = {0:1}
    for i in range(len(nums)):
        summ += nums[i]
        # the in operator is O(1) for dictionaries and sets in python
        if summ - k in prefixSum:
            # https://youtu.be/fFVZt-6sgyo?t=633
            res += prefixSum[summ - k]
        prefixSum[summ] = prefixSum.get(summ, 0) + 1
    return res

# see why res += prefixSum[summ - k] and not res += 1 in python tutor
print(subarray_sum_equals_k([1,-1,0],0))
print(subarray_sum_equals_k([1,1,-1,1,1,1,-1,-1,1,1,-1,1,-1],2))


# Let's do an example with nums = [2,3,4,5] and k = 9.

# i = 0, nums[i] = 2, summ = 2, summ - k = -7, res = 0, prefixSum = {0:1, 2:1}
# i = 1, nums[i] = 3, summ = 5, summ - k = -4, res = 0, prefixSum = {0:1, 2:1, 5:1}
# i = 2, nums[i] = 4, summ = 9, summ - k = 0, res = 1, prefixSum = {0:1, 2:1, 5:1, 9:1}
# i = 3, nums[i] = 5, summ = 14, summ - k = 5, res = 2, prefixSum = {0:1, 2:1, 5:1, 9:1, 14:1}

# res = 2

    # So why aren't we using set instead of dictionary if value for each key is gonna be 1? Or just use res += 1

        # It's not. The the numbers can be negative so you can have the same prefix sum multiple times. Just not in my example.