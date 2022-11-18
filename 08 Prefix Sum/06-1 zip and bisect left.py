# source: https://github.com/python/cpython/blob/f4c03484da59049eb62a9bf7777b963e2267d187/Lib/bisect.py

def bisect_left(arr, val):
    lo, hi = 0, len(arr)-1
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < val:
            lo = mid + 1
        else:
            hi = mid
    return lo

a = [1,3,5,7,9]
print(bisect_left(a, 2))


# https://www.reddit.com/r/learnpython/comments/ykywsi/comment/iuvo4b8/?context=3

# * here is the unpacking operator. It passes each element of matrix (i.e. each row) as a separate argument to zip.
# zip creates an iterable of tuples that contain one element from each of the passed iterables. 

grid = [[1,2,3],
        [4,5,6],
        [7,8,9]]

a = zip(grid)
b = zip(*grid)

print(list(a))
print(list(b))