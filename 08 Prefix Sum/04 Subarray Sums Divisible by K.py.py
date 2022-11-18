# LC: https://leetcode.com/problems/subarray-sums-divisible-by-k/

def f(nums, k):
    res = 0
    h = {0:1}
    presum = 0
    for i in range(len(nums)):
        presum += nums[i]
        remainder = presum % k
        if remainder in h:
            res += h[remainder]
        h[remainder] = h.get(remainder, 0) + 1
    return res

print(f([4,5,0,-2,-3,1], 5))