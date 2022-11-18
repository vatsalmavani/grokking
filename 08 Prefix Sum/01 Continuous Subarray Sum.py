# LC: https://leetcode.com/problems/continuous-subarray-sum/
# NC: https://youtu.be/OKcrLfR-8mE

def brute_force(nums, k):
    for i in range(len(nums)):
        summ = nums[i]
        for j in range(i+1, len(nums)):
            summ += nums[j]
            check = summ % k
            if check == 0:
                return True
    return False

nums = [23,2,4,6,7]; k = 6
print(brute_force(nums, k))
nums = [23,2,6,4,7]; k = 6
print(brute_force(nums, k))
nums = [23,2,6,4,7]; k = 13
print(brute_force(nums, k))

def prefix_sum(nums, k):
    prefixSum = 0
    hashtable = {0:-1}
    for i in range(len(nums)):
        prefixSum += nums[i]
        remainder = prefixSum % k
        if remainder not in hashtable:
            hashtable[remainder] = i
        elif i - hashtable[remainder] > 1:
            return True
    return False

# try this test case in poython tutor with hashtable = {} instead of 0:-1
nums = [23,2,4,6,6]; k = 7
print(prefix_sum(nums, k))
# try this test case in poython tutor with hashtable = {0:0} instead of 0:-1
nums = [2,4,3]; k = 6
print(prefix_sum(nums, k))


def f(nums, k):
    prefs = 0
    h = {0:-1}
    for i in range(len(nums)):
        prefs += nums[i]
        val = prefs % k
        if (prefs - k) % k in h:
            if i - h[(prefs - k) % k] > 1:
                return True
        if val not in h:
            h[val] = i
    return False