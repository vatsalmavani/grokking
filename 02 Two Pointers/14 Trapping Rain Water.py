# LC: https://leetcode.com/problems/trapping-rain-water/
# NC: https://youtu.be/ZI2z5pq0TqA

# this is O(n) time and space solution
# the two pointer approach neetcode shows is O(n) time and O(1) space
# but you'll understand it only if you understand this approach

def trap(height):
    maxLeft = [0]*len(height)
    mxLeft = 0
    maxRight = [0]*len(height)
    mxRight = 0
    minLR = [0]*len(height)
    for l in range(len(height)):
        if l > 0 and height[l-1] > mxLeft:
            mxLeft = height[l-1]
        maxLeft[l] = mxLeft
    # print(maxLeft)
    for r in range(len(height)-1, -1, -1):
        if r < len(height) - 1 and height[r+1] > mxRight:
            mxRight = height[r+1]
        maxRight[r] = mxRight
    # print(maxRight)
    for i in range(len(height)):
        minLR[i] = min(maxLeft[i], maxRight[i])
    # print(minLR)
    
    res = 0
    for i in range(len(height)):
        if minLR[i] - height[i] > 0:
            res += minLR[i] - height[i]
    
    return res

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap([4,2,0,3,2,5]))

####### SHORT AND SWEET CODE #######

# O(n) time and O(n) space
def rain(height):
    n = len(height)
    lmax, rmax, minlr = [0]*n, [0]*n, [0]*n
    for i in range(1,n):
        lmax[i] = max(lmax[i-1], height[i-1])   # since lmax[i-1] is max left till now
    for i in range(n-2,-1,-1):
        rmax[i] = max(rmax[i+1], height[i+1])   # since rmax[i+1] is max right till now
    for i in range(n):
        minlr[i] = min(lmax[i], rmax[i])
    count = 0
    for i in range(n):
        if minlr[i] - height[i] > 0:
            count += minlr[i] - height[i]
    return count

# two pointers: O(n) time and O(1) space
def rain(height):
    if not height: return 0

    l,r = 0, len(height)-1
    leftMax, rightMax = height[l], height[r]
    res = 0
    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]
    return res