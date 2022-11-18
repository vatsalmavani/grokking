# LC: https://leetcode.com/problems/insert-interval/
# grokking (this code explained nicely): https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743628532_22Unit
# neetcode: https://youtu.be/A8NUOmlwOlM

# approach 1: O(nlogn) time:

# If the given list was not sorted, we could have simply appended the new interval to it and used the merge() function from Merge Intervals.
# But since the given list is sorted, we should try to come up with a solution better than O(N*logN)


# approach 2: O(n) time and O(n) space

def insert(intervals, newInterval):
    merged = []
    i, start, end = 0, 0, 1

    # skip (and add to output) all intervals that come before the 'new_interval'
    while i < len(intervals) and intervals[i][end] < newInterval[start]:
        merged.append(intervals[i])
        i += 1

    # merge all intervals that overlap with 'new_interval'
    while i < len(intervals) and newInterval[start] <= intervals[i][end] and intervals[i][start] <= newInterval[end]:  # this condition is actually: intervals[i][end] >= new_interval[start] and intervals[i][start] <= new_interval[end] but since first condition is fulfilled due to previous while loop condn, we didn't write this condn
        newInterval[start] = min(intervals[i][start], newInterval[start])
        newInterval[end] = max(intervals[i][end], newInterval[end])
        i += 1

    # insert the new_interval
    # if merging happened then fine but if not, (eg. [[1,2], [5,6]] and new = [3,4]) add new_interval anyway
    merged.append(newInterval)

    # add all the remaining intervals to the output
    while i < len(intervals) and intervals[i][start] > newInterval[end]:
        merged.append(intervals[i])
        i += 1
    return merged


def main():
    print("Intervals after inserting the new interval: " + 
            str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " + 
            str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " + 
            str(insert([[2, 3], [5, 7]], [1, 4])))
    print(insert([[2,3], [4,5]], [0,1]))


main()



# same code
def f(intervals, new):
    i = 0
    res = []
    while i < len(intervals) and intervals[i][1] < new[0]:
        res.append(intervals[i])
        i += 1
    
    while i < len(intervals) and new[1] >= intervals[i][0]:
        new[0] = min(new[0], intervals[i][0])
        new[1] = max(new[1], intervals[i][1])
        i += 1
    res.append(new)

    while i < len(intervals):
        res.append(intervals[i])
        i += 1
    
    return res