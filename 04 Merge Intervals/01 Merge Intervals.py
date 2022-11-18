# LC: https://leetcode.com/problems/merge-intervals/
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743622133_21Unit
# second code: https://youtu.be/5EY9rHCfa8g
# neetcode (same as second code, but explained by neetcode): https://youtu.be/44H3cEC2fFM

# same code concept, slightly different code: code 2

def mergeIntervals(intervals):
    if len(intervals) < 2:
        return intervals
    
    intervals.sort()    # automatically sorted by first value
    res = [intervals[0]]
    # slicing a list is O(k) time and space where k is length of the slice
    # hence, intervals[1:] is O(n) time and space
    # this is why, to decrease time and space, we can use
    # for i in range(1, len(intervals))
    # but in most cases it won't matter since we will already have O(n) time and space
    for interval in intervals[1:]:
        if interval[0] > res[-1][1]:    # interval[0] means start of next interval. res[-1][1] means end of the current interval
            res.append(interval)
        else:
            res[-1][1] = max(res[-1][1], interval[1])   # if they overlap, end should be max from last interval's end and current interval's end
    return res

print(mergeIntervals([[1,4], [2,6], [7,9]]))

# grokking: code 1
def merge(intervals):
    if len(intervals) < 2:
        return intervals
    
    intervals.sort(key = lambda x:x[0])

    mergedIntervals = []
    start = intervals[0][0]
    end = intervals[0][1]
    for i in range(1, len(intervals)):
        interval = intervals[i]
        intervalStart = interval[0]
        intervalEnd = interval[1]
        if intervalStart <= end:     # if current start is less than previous end i.e. current start overlapes with previous end
            end = max(intervalEnd, end)
        else:
            mergedIntervals.append([start, end])
            start = intervalStart
            end = intervalEnd
    mergedIntervals.append([start, end])
    return mergedIntervals

print(merge([[1,4], [2,6], [7,9]]))

# sorting - O(nlogn) time; iterating over intervals (for loop) - O(n) time
# hence total time = O(nlogn)
# sorting - O(n) space; result - O(n) space; hence total O(n) space