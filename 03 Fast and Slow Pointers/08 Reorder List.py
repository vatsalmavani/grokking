# LC: https://leetcode.com/problems/reorder-list/
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743587877_18Unit
# neetcode: https://youtu.be/S5bfdUTrKLM


from collections import deque


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# approach 1: O(n) time and O(1) space

def reorder(head):
    # find middle
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # reverse second half
    prev = None
    while slow:
        next = slow.next
        slow.next = prev
        prev = slow
        slow = next
    
    # merge the two linked lists
    ptr1, ptr2 = head, prev  # heads of first ll and second ll
    while ptr1 and ptr2:
        next1, next2 = ptr1.next, ptr2.next
        ptr1.next = ptr2
        ptr2.next = next1
        ptr1 = next1
        ptr2 = next2
    if ptr1:  # if first is not none means if there is a cycle # see in python tutor with following input without this if statement
        ptr1.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
reorder(head)


# another intuitive approach: O(n) time and O(n) space
# link: https://www.youtube.com/watch?v=To_uAJRu8NQ

'''
using double ended queue:
say 1,2,3,4,5,6,7 is our linked list
append to queue from second element: 2,3,4,5,6,7
pop from last: 7
add next to 1: 1,7
pop from left: 2
add next to 7: 1,7,2
and so on
'''

def reorder_using_queue(head):
    node = head.next    # since we want to append everything from the second element and not the first one
    q = deque()
    
    # fill the queue
    while node:
        q.append(node)
        node = node.next

    # pop from right and then left until the queue is empty
    while q:
        if head:
            temp = q.pop()
            head.next = temp
            head = head.next
        if head and q:  # we have to check whether q is empty or not since the previous if condition may have caused the queue to become empty
            temp = q.popleft()
            head.next = temp
            head = head.next
    head.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
reorder_using_queue(head)