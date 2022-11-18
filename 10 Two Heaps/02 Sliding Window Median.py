# LC: https://leetcode.com/problems/sliding-window-median/
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628744001784_63Unit
# this code: https://youtu.be/NT5Lp5vaMm0
# https://youtu.be/lXY2oiDlc1E

from heapq import heappop, heappush, heapify


# usual sliding window format
from heapq import heappush, heappop, heapify

def f(nums, k):
    minHeap, maxHeap = [], []
    res = []
    l = 0
    for r in range(len(nums)):
        heappush(minHeap, nums[r])
        heappush(maxHeap, -heappop(minHeap))
        if len(maxHeap) > len(minHeap):
            heappush(minHeap, -heappop(maxHeap))
        
        if r-l+1 > k:
            def remove(heap, elem):
                idx = heap.index(elem)
                del heap[idx]
                heapify(heap)
            if nums[l] <= -maxHeap[0]:
                remove(maxHeap, -nums[l])
            else:
                remove(minHeap, nums[l])
            l += 1
        
            if len(maxHeap) > len(minHeap):
                heappush(minHeap, -heappop(maxHeap))
            elif len(minHeap) > len(maxHeap) + 1:
                heappush(maxHeap, -heappop(minHeap))

        if r-l+1 == k:
            if k % 2 == 1:
                res.append(minHeap[0])
            else:
                res.append((minHeap[0] - maxHeap[0])/2)
    return res

print(f([1,3,-1,-3,5,3,6,7], 3))

# time: O(n*k)
# space: O(k)


def medianSlidingWindow(nums, k):
    minHeap, maxHeap = [], []
    res = []
    for i in range(len(nums)):
        # balancing
        heappush(minHeap, nums[i])
        heappush(maxHeap, -heappop(minHeap))
        if len(maxHeap) > len(minHeap):
            heappush(minHeap, -heappop(maxHeap))
            
        # remove the left element going out of the window
        def remove(heap, etbr):
            idx = heap.index(etbr)
            del heap[idx]
            heapify(heap)   # heapify is O(n) time. here, O(k) since len(heap) is k

        if len(minHeap) + len(maxHeap) > k:
            elem = nums[i-k]  # elementToBeRemoved
            if elem <= -maxHeap[0]:
                remove(maxHeap, -elem)
            else:
                remove(minHeap, elem)

        # rebalance
        if len(maxHeap) > len(minHeap):
            heappush(minHeap, -heappop(maxHeap))
        elif len(minHeap) > len(maxHeap) + 1:
            heappush(maxHeap, -heappop(minHeap))

        # appending medians
        if len(minHeap) + len(maxHeap) == k:
            if k % 2 == 1:
                res.append(minHeap[0])
            else:
                tmp = minHeap[0]/2 - maxHeap[0]/2
                res.append(tmp)

    return res

print(medianSlidingWindow(nums = [1,2,3,4,2,3,1,4,2], k = 3))