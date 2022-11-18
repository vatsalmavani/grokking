# LC: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
# approach 1 & 2: https://www.youtube.com/watch?v=6792BoQIgko
# approach 3: https://www.youtube.com/watch?v=hi9Z7EdsEfw

# approach 1: sorting
# time: O(n*logn) for sorted(nums)
# space: O(n) for nums2
def shortestSubBySorting(nums):
    nums2 = sorted(nums)
    l,r = len(nums), 0
    for i in range(len(nums)):
        if nums[i] != nums2[i]:
            l = min(l, i)
            r = max(r, i)
    if l == len(nums): return 0     # array is already sorted
    return r-l+1

# approach 2: stack
# time = space = O(n)

# approach 3: intuitive
# time: O(n) & space: O(1)
def shortestSub(nums):
    mn, mx = float('inf'), float('-inf')

    for i in range(1,len(nums)):
        if nums[i] < nums[i-1]:
            mn = min(mn, nums[i])
    
    for i in range(len(nums)-2,-1,-1):
        if nums[i] > nums[i+1]:
            mx = max(mx, nums[i])
        
    if mn == float('inf'): return 0

    for l in range(len(nums)):
        if nums[l] > mn:
            break
    for r in range(len(nums)-1, -1, -1):
        if nums[r] < mx:
            break

    return r-l+1

print(shortestSub([6,5,1,2,4,3,7,8,9]))
# visualize these examples in python tutor if you don't understand the algo
print(shortestSub([1,2,4,5,3]))
print(shortestSub([1,2,7,8,3,6,9,4]))



###########################################################################

def f(nums):
    smallest, biggest = (float('inf'), 0), (float('-inf'), len(nums)-1)

    # find min
    for i in range(1,len(nums)):
        if nums[i] < nums[i-1]:
            smallest = min((nums[i],i), smallest)
    
    # find max
    for i in range(len(nums)-2,-1,-1):
        if nums[i] > nums[i+1]:
            biggest = max((nums[i], i), biggest)
    
    # if there is any element bigger than smallest[0], it is our left pointer
    l = smallest[1]
    for i in range(smallest[1]):
        if nums[i] > smallest[0]:
            l = i
            break
    
    # opposite for max
    r = biggest[1]
    for i in range(len(nums)-1, biggest[1], -1):
        if nums[i] < biggest[0]:
            r = i
            break
    
    return 0 if l == smallest[1] and r == biggest[1] else r-l+1

print(f([1]))