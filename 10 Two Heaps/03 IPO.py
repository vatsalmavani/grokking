# LC: https://leetcode.com/problems/ipo/
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628744008443_64Unit

from heapq import heappush, heappop


def maximized_capital(capitals, profits, no_of_projects, initial_capital):
    minCapitalHeap = []
    maxProfitHeap = []

    for i in range(len(capitals)):
        heappush(minCapitalHeap, (capitals[i], i))
    
    available_capital = initial_capital
    for _ in range(no_of_projects):
        while minCapitalHeap and minCapitalHeap[0][0] <= available_capital:
            capital, i = heappop(minCapitalHeap)    # we can select one project only once that's why pop
            heappush(maxProfitHeap, -profits[i])
        if not maxProfitHeap:
            break
        available_capital += -heappop(maxProfitHeap)
    return available_capital

# time: O(nlogn + klogn)
'''
the code is:
for i in range(n):  # --> O(nlogn)
    heappush(heap)  # --> O(logn)
for _ in range(k):
    # len(heap) = n
    while heap and condition:   # --> O(nlogn)
        heappop(heap)   # --> O(logn) happens for n times in total
    # len(heap2) = n
    heappop(heap2)  # --> O(logn) happens for k times for range(k)
'''
# space: O(n)