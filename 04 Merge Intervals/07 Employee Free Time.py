# lintcode: https://www.lintcode.com/problem/850/
# in lintcode examples, input is represented like this: [[1,2,5,6],[1,3],[4,10]] but should be like this: [[[1,2],[5,6]],[[1,3]],[[4,10]]]
# each 2d array represents one employee's intervals
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743666558_27Unit



# grokking approach 1: O(nlogn) time, O(n) space; n = no. of intervals
# approach: make a list of all the intervals, sort them by start time and iterate through these intervals, and whenever we find non-overlapping intervals (e.g., [2,4] and [6,8]), we can calculate a free interval (e.g., [4,6]).

def find_free_time(schedule):
    ls = []
    for intervals in schedule:  # -------> O(n) (two for loops combined); n = total number of intervals
        for interval in intervals:
            ls.append(interval)

    ls.sort()   # --------> O(nlogn)
    merged = [ls[0]]
    for start, end in ls[1:]:   # ------> O(n)
        if start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    
    res = []
    for i in range(1, len(merged)):     # O(n)
        if merged[i-1][1] < merged[i][0]:
            res.append([merged[i-1][1], merged[i][0]])
    return res

print(find_free_time([[[1,3]], [[2,4]], [[3,5], [7,9]]]))


# same approach, same complexity, reduced one for loop
def find_free_time2(schedule):
    ls = []
    for intervals in schedule:
        for interval in intervals:
            ls.append(interval)

    ls.sort()
    res = []
    # check if starting time of next interval is before the end time of current interval
    max_end_time = ls[0][1]
    for i in range(1, len(ls)):
        # overlapping intervals
        if ls[i][0] <= max_end_time:
            max_end_time = max(max_end_time, ls[i][1])
        else:   # found a gap
            res.append([max_end_time, ls[i][0]])
            max_end_time = max(max_end_time, ls[i][1])  # this is basically max_end_time = ls[i][1] since ls[i][1] is always > than max_end_time in this case
    return res

print(find_free_time2([[[1,3], [9,12]], [[2,4]], [[6,8]]]))



# grokking approach 2: O(nlogk) time, O(n) space
# do this approach too if you like