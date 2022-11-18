# LC: https://leetcode.com/problems/3sum-closest/
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743457252_5Unit
# youtube (this code: 2nd one): https://www.youtube.com/watch?v=Sk3Mh2699-o

# basically the same code as below, just with better variable names
def f(nums, target):
    nums.sort()
    dist = float('inf')  # this is the smallest distance found: minDist is a better name
    for i in range(len(nums)):
        l,r = i+1, len(nums)-1
        while l < r:
            summ = nums[i] + nums[l] + nums[r]
            if abs(dist) > abs(target - summ):
                dist = target - summ
            if summ < target: l += 1
            else: r -= 1
    return target - dist

print(f([-1,2,-4,1,3], 5))


# optimised code: the above code gives (almost) TLE when submitted. This code is better than 46% in time
def threeSumClosest(nums, target):
    nums.sort()
    distance = float('inf')

    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        l, r = i+1, len(nums)-1
        new_target = target - nums[i]
        while l < r:
            sum_val = nums[l] + nums[r]
            
            if abs(distance) > abs(new_target - sum_val):   # abs is imp bcoz what if sum_val > new_target?
                distance = new_target - sum_val

            if sum_val == new_target:
                return target
            elif sum_val > new_target:
                r -= 1
            else:
                l += 1

    return target - distance

nums = [-2, 0, 1, 2]; target=2
print(threeSumClosest(nums, target))