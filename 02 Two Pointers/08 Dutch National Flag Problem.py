# LC: https://leetcode.com/problems/sort-colors/
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743488620_8Unit
# solution: https://www.youtube.com/watch?v=sEQk8xgjx64

# we can brute force in O(N^2) time
# we can use sorting algo like heapsort or merge sort in O(n*logn) time
# but we want to solve this prob in O(n) time

def dutch(nums):
    # three pointers - low, mid, high
    l,m,h = 0,0,len(nums)-1
    while m <= h:
        if nums[m] == 0:
            nums[l], nums[m] = nums[m], nums[l]
            m += 1
            l += 1
        elif nums[m] == 1:
            m += 1
        else:
            nums[m], nums[h] = nums[h], nums[m]
            h -= 1
    return nums

print(dutch([0,1,2,0,1,2]))