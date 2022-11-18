# LC 325
# lintcode: https://www.lintcode.com/problem/911/

def max_sub_sum_equals_k(nums, k):
    summ = maxlen = 0
    # in this hashtable: key = prefix sum, value = index
    hashtable = {0:-1}
    for i in range(len(nums)):
        summ += nums[i]
        if summ - k in hashtable:
            maxlen = max(maxlen, i - hashtable[summ - k])
        if summ not in hashtable:
            hashtable[summ] = i
    return maxlen

nums = [1, -1, 5, -2, 3]; k = 3
print(max_sub_sum_equals_k(nums, k))
nums = [1, 1, 1, 2, 3]; k = 3
print(max_sub_sum_equals_k(nums, k))
nums = [-1]; k = -1
print(max_sub_sum_equals_k(nums, k))