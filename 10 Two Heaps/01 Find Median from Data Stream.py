# LC: https://leetcode.com/problems/find-median-from-data-stream/
# grokking (this code): https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743994867_62Unit

# brute force

class MedianFinder:
    def __init__(self):
        self.ls = []
        
    def addNum(self, num: int) -> None:
        self.ls.append(num)
        self.ls.sort()
        
    def findMedian(self) -> float:
        n = len(self.ls)
        if n % 2 == 0:
            return (self.ls[n//2] + self.ls[(n//2)-1])/2
        else:
            return self.ls[n//2]
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# addNum --> o(nlogn) time



# optimised brute force (O(n) time for adding)
# accepted on leetcode

from bisect import insort


class MedianFinderInsort:
    def __init__(self):
        self.ls = []

    def addNum(self, num):
        insort(self.ls, num)

    def findMedian(self) -> float:
        n = len(self.ls)
        if n % 2 == 0:
            return (self.ls[n//2] + self.ls[(n//2)-1])/2
        else:
            return self.ls[n//2]



# two heap method (O(logn) time for adding)

# this code: https://youtu.be/NT5Lp5vaMm0
from heapq import heappop, heappush


class MedianFinder:
    def __init__(self) -> None:
        self.minHeap, self.maxHeap = [], []

    def addNum(self, num):
        heappush(self.minHeap, num)
        heappush(self.maxHeap, -heappop(self.minHeap))
        if len(self.maxHeap) > len(self.minHeap):
            heappush(self.minHeap, -heappop(self.maxHeap))
    
    def findMedian(self):
        if len(self.maxHeap) == len(self.minHeap):
            return -self.maxHeap[0]/2 + self.minHeap[0]/2
        return self.minHeap[0]
    
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
obj.addNum(3)
print(obj.findMedian())


# grokking solution
class MedianFinderTwoHeap:
    def __init__(self) -> None:
        self.maxHeap, self.minHeap = [], []
    
    def addNum(self, num):
        # push num to one of the heaps
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

        # balance the lengths of the heaps
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))
        
    def findMedian(self):
        if len(self.maxHeap) == len(self.minHeap):
            return -self.maxHeap[0]/2 + self.minHeap[0]/2
        return -self.maxHeap[0]

# addNum = O(logn) time
# findMedian = O(1) time
# overall algo = O(n) space