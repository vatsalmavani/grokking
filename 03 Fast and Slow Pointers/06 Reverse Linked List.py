# LC: https://leetcode.com/problems/reverse-linked-list/
# neetcode: https://youtu.be/G0_I-ZF0S38

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# recursive approach: O(n) time and O(n) space
def reverseListRecursive(head):
    if not head:
        return None
    
    newHead = head
    if head.next:
        newHead = reverseListRecursive(head.next)
        head.next.next = head
    head.next = None

    return newHead

# visualize in python tutor
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
reverseListRecursive(head)


# iterative approach: O(n) time and O(1) space
def reverseListIterative(head):
    prev, curr = None, head
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

reverseListIterative(head)