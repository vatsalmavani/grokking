# lintcode: https://www.lintcode.com/problem/919/
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743654901_25Unit
# neetcode: https://youtu.be/FdzJmTCVyJU
# deepti (explains why we need min heap or why we need to sort end time): https://youtu.be/tNhiD4SaumY


# neetcode solution
def meeting_rooms(intervals):
    start = sorted(i[0] for i in intervals)
    end = sorted(i[1] for i in intervals)

    res, count = 0,0
    s,e = 0,0
    while s < len(intervals):
        if start[s] < end[e]:
            s += 1
            count += 1
        else:
            e += 1
            count -= 1
        res = max(res, count)
    return res



# grokking solution
from heapq import *

def min_meeting_rooms(meetings):
    # sort the meetings by start time
    meetings.sort()

    minRooms = 0
    # minHeap represents all the meeting's end times which are currently taking place
    # we are using minHeap to find minimum end time in O(logn) time
    minHeap = []
    for start, end in meetings:
        # remove all the meetings that have ended
        while minHeap and (minHeap[0] <= start):
            heappop(minHeap)
        # add the current meeting into min_heap
        heappush(minHeap, end)
        # all active meetings are in the min_heap, so we need rooms for all of them.
        minRooms = max(minRooms, len(minHeap))
    return minRooms

# time complexity: O(nlogn) due to sorting + heappop & heappush takes O(logn) and it happens for every meeting hence O(nlogn)
# space comp: O(n) due to sorting + in worst case, when all meetings overlap, heap will have n meetings in it



#  Given a list of intervals, find the point where the maximum number of intervals overlap.
from heapq import *

def f(meetings):
    meetings.sort()
    res = 0
    minHeap = []
    ans = 0
    for start, end in meetings:
        while minHeap and (minHeap[0][0] <= start):
            heappop(minHeap)
        heappush(minHeap, (end, start))
        if len(minHeap) > res:
            ans = start
        res = max(res, len(minHeap))
    return ans

# [0,1,2,3,4,5,6,7,8,9]
#  |-------| |---|
#    |-----|     |---|
#      |-----|

print(f([[0,4], [1,4], [2,5], [5,7], [7,9]]))