# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743469029_6Unit
# lintcode: https://www.lintcode.com/problem/918/

# repeated subarrays are also counted in this code but this is the one they are accepting
# eg. [-2,-1,-1,0,1,1,1] will give repeated arrays in res
def threesumSmaller(nums, target):
    nums.sort()
    count = 0
    res = []
    for i in range(len(nums) - 2):
        l,r = i+1, len(nums) - 1
        while l < r:
            cursum = nums[i] + nums[l] + nums[r]
            if cursum >= target:
                r -= 1
            else:
                count += r-l
                for j in range(r, l, -1):
                    res.append([nums[i], nums[l], nums[j]])
                l += 1
    print(count)
    print(res)

threesumSmaller([-2,-1,-1,0,1], 0)



##############################################################################



def smaller3sum(nums, target):
    nums.sort()
    count = 0
    for i in range(len(nums) - 2):
        l, r = i+1, len(nums) -1
        new_target = target - nums[i]
        while l < r:
            cur_sum = nums[l] + nums[r]
            if cur_sum < new_target:    # found the triplet
                count += r - l  # since arr[right] >= arr[left], therefore, we can replace arr[right] by any number between left and right to get a sum less than the target sum
                l += 1
            else:
                r -= 1
    return count

nums = [-1, 0, 2, 3]; target=3
print(smaller3sum(nums, target))

nums = [-1, 4, 2, 1, 3]; target=5
print(smaller3sum(nums, target))

# time complexity = O(n^2)  # O(n*logn (for sorting) + n^2 (for + while loops))
# space complexity = O(n) for sorting


##############################################################################


# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743469029_6Unit

# Write a function to return the list of all such triplets instead of the count. How will the time complexity change in this case?

def smaller3sumVarient(nums, target):
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        new_target = target - nums[i]
        l, r = i+1, len(nums)-1
        while l < r:
            cur_sum = nums[l] + nums[r]
            if cur_sum < new_target:
                # this part is changed
                for x in range(r, l, -1):
                    res.append([nums[i], nums[l], nums[x]])
                l += 1
            else:
                r -= 1
    return res

nums = [-1, 0, 2, 3]; target=3
print(smaller3sumVarient(nums, target))

nums = [-1, 4, 2, 1, 3]; target=5
print(smaller3sumVarient(nums, target))

# this will technically take O(n^3) time complexity but it is better than brute force (with 3 nested loops) time complexity of O(N^3)