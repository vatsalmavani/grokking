# lintcode: Meeting Rooms - https://www.lintcode.com/problem/920/
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743642980_24Unit

def can_attend_meetings(intervals):
    intervals.sort(key=lambda x: x[0])
    start, end = 0, 1
    for i in range(1, len(intervals)):
        # meeting 2 starts before meeting 1 ends
        if intervals[i][start] < intervals[i-1][end]:
            # please note the comparison above, it is "<" and not "<="
            # while merging we needed "<=" comparison, as we will be merging the two
            # intervals having condition "intervals[i][start] == intervals[i - 1][end]" but
            # such intervals don't represent conflicting appointments as one starts right
            # after the other
            return False
    return True

# due to sorting:
# time: O(n*logn)
# space: O(1)