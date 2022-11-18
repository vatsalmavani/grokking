# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743662085_26Unit

import heapq

def max_cpu_load(jobs):
    jobs.sort()
    max_load = 0
    cur_load = 0
    cur_jobs = []   # min heap
    for start, end, load in jobs:
        while cur_jobs and cur_jobs[0][0] <= start:
            cur_load -= cur_jobs[0][1]
            heapq.heappop(cur_jobs)
        heapq.heappush(cur_jobs, [end, load])
        cur_load += load
        max_load = max(max_load, cur_load)
    return max_load

print(max_cpu_load([[1,4,3], [2,5,4], [7,9,6]]))
print(max_cpu_load([[6,7,10], [2,4,11], [8,12,15]]))
print(max_cpu_load([[1,4,2], [2,4,1], [3,6,5]]))

# time: O(nlogn) where n = total number of jobs - sorting: O(nlogn; heappop, heappush: O(logk) where k is number of elements in heap atm. worst case: O(logn) happens for n times in the loop: O(nlogn)
# space: sorting: O(n); in worst case all elements in heap: O(n)