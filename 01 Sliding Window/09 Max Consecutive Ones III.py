# LC: https://leetcode.com/problems/max-consecutive-ones-iii/
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628541045705_5Unit
# this solution exaplanation: https://www.youtube.com/watch?v=1X6U1DoAd2w

def findLength(arr, k):
    if arr == None or len(arr) == 0 or k<0:
        return -1
    if k >= len(arr):
        return len(arr)
    
    max_length = 0
    num_zero = 0

    l = 0
    for r in range(len(arr)):
        if arr[r] == 0:
            num_zero += 1
        while num_zero > k: # we can put if statement here instead of while but if you dryrun a3, k3 on whiteboard, while is more intuitive
            if arr[l] == 0:
                num_zero -= 1
            l += 1
        max_length = max(max_length, r-l+1)
    return max_length

a1 = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
k1 = 2
a2 = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
k2 = 3
a3 = [1,0,0,1,0,1,1,0,1,1,1]
k3 = 2

print(findLength(a1,k1))
print(findLength(a2,k2))