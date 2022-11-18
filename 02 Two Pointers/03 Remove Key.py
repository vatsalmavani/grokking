# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743424499_2Unit
# in similar questions section

def removeKey(arr, key):
    l = 0
    for r in range(len(arr)):
        if arr[r] != key:
            arr[l] = arr[r]
            l += 1
    return l

arr = [3, 2, 3, 6, 3, 10, 9, 3]; key = 3
print(removeKey(arr, key))
print(arr)