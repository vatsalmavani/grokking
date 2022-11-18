# LC: https://leetcode.com/problems/minimum-interval-to-include-each-query/
# NC: https://youtu.be/5hQ5WWW5awQ

from heapq import heappop, heappush


def brute_force(intervals, queries):
    res = []
    # iterate over intervals for each query and find the minimum interval length
    for query in queries:
        min_length = float('inf')
        for start, end in intervals:
            if start <= query <= end:
                min_length = min(min_length, end - start + 1)
        res.append(-1) if min_length == float('inf') else res.append(min_length)
    return res

intervals = [[1,4],[2,4],[3,6],[4,4]]; queries = [2,3,4,5]
print(brute_force(intervals, queries))

# time complexity: O(m*n); m = len(intervals), n = len(queries)
# time limit exceeded in leetcode



def neetcode(intervals, queries):
    intervals.sort()
    res = {}
    i = 0
    minHeap = []

    for q in sorted(queries):
        # add all the intervals to minHeap which start before the query q
        while i < len(intervals) and intervals[i][0] <= q:
            l,r = intervals[i]
            heappush(minHeap, (r-l+1, r))
            i += 1
        
        # remove all the intervals which have ended before the query q
        while minHeap and minHeap[0][1] < q:
            heappop(minHeap)
        
        res[q] = minHeap[0][0] if minHeap else -1

    # since res is hashmap, we have to convert it to list
    return [res[q] for q in queries]

# time complexity O(nlogn + qlogq) : n = len(intervals); q = len(queries)

# this is bcoz this code is:
# for n in sorted(array of length n):
#     some work that takes O(m) time when the for loop is finished
# hence the time of this for loop is: O(nlogn + m)