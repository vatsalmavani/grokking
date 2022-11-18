# LC: https://leetcode.com/problems/interval-list-intersections/
# grokking (this code): https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743634893_23Unit

# in leetcode constraints, it is given that end(i) < start(i+1)
# this means: intervals are disjoint (non overlapping with its own elements) sorted on their start time

def intersection_brute_force(firstList, secondList):
    res = []
    start, end = 0, 1

    # we are iterating through list1 and seeing if any element of list2 is intersecting or not
    for i in range(len(firstList)):
        for j in range(len(secondList)):
            # ignore all the intervals in list2 which are after end of interval[i] of list1
            if secondList[j][start] > firstList[i][end]:
                continue
            # ignore all the intervals of list2 which are ending before the starting of interval[i] of list1
            if firstList[i][start] > secondList[j][end]:
                continue
            # now after above two conditions, both lists remaining are intersecting
            s = max(firstList[i][start], secondList[j][start])
            e = min(firstList[i][end], secondList[j][end])
            res.append([s,e])
    return res

# time complexity: O(M*N); where M & N are lengths of firstlist and secondlist
# space complexity: O(1) if we ignore the space required by res otherwise O(max(M,N))

def intersection_grokking(intervals_a, intervals_b):
    res = []
    i,j = 0,0
    start, end = 0, 1

    while i < len(intervals_a) and j < len(intervals_b):
        
        # check if two intervals intersect
        a_overlaps_b = intervals_b[j][start] <= intervals_a[i][start] <= intervals_b[j][end]
        b_overlaps_a = intervals_a[i][start] <= intervals_b[j][start] <= intervals_a[i][end]

        # store the intersection in result
        if a_overlaps_b or b_overlaps_a:
            res.append([max(intervals_a[i][start], intervals_b[j][start]),\
                min(intervals_a[i][end], intervals_b[j][end])])
        
        # move to the next interval which is finishing first
        if intervals_a[i][end] < intervals_b[j][end]:
            i += 1
        else:
            j += 1
    
    return res

# As we are iterating through both the lists once, the time complexity of the above algorithm is O(N + M), where ‘N’ and ‘M’ are the total number of intervals in the input arrays respectively.
# Ignoring the space needed for the result list, the algorithm runs in constant space O(1).


# if connecting starting and ending points of the two different intervals intersect, then the two intervals are intersecting
def f(a, b):
    res = []
    i,j = 0,0
    while i < len(a) and j < len(b):
        if a[i][0] <= b[j][1] and a[i][1] >= b[j][0]:
            res.append([max(a[i][0], b[j][0]), min(a[i][1], b[j][1])])
        if a[i][1] < b[j][1]:
            i += 1
        else:
            j += 1
    return res