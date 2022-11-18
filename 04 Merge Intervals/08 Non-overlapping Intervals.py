# leetode: https://leetcode.com/problems/non-overlapping-intervals/
# neetcode: https://youtu.be/nONCGxWoUfM

def overlappingIntervals(intervals):
    intervals.sort()
    res = 0     # how many intervals need to be removed?
    prevEnd = intervals[0][1]   # end of first interval
    for start, end in intervals[1:]:
        # not overlapping
        if start >= prevEnd:
            prevEnd = end   # since end is definetly > than previous end
        # intervals overlapping
        else:
            res += 1    # since intervals overlapping, we need to remove one interval
            prevEnd = min(prevEnd, end) # in the following example, understand this by these intervals: [[11,16], [12,13], [14,15]]
    return res

intervals = [[0,1], [2,5], [3,6], [4,5], [6,8], [7,10], [9,11], [11,16], [12,13], [14,15]]
print(overlappingIntervals(intervals))

# [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
#  |-| |-----| |---| |-----| |---| |---|
#        |-----| |------|  |--------------|
#          |-| 