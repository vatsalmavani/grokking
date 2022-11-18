# LC: https://leetcode.com/problems/reverse-nodes-in-k-group/
# NC: https://youtu.be/1UOPsfP85V4
# striver: https://youtu.be/Of0HPkk3JgI
# do NOT reverse the groups with len(group) < k

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def f(head, k):
    dummy = Node(0, head)
    tmp = head
    count = 1
    while tmp.next:
        tmp = tmp.next
        count += 1
    
    prev, curr = dummy, head
    while count >= k:
        end_prev = prev
        start_cur = curr

        # get next group's start
        start_next = start_cur
        i = 0
        while i < k:
            start_next = start_next.next
            i += 1
        
        # reverse
        i = 0
        prev, curr = start_next, start_cur
        while i < k:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            i += 1

        # connect and update nodes
        end_prev.next = prev
        prev = start_cur
        count -= k

    return dummy.next

head = Node(1, Node(2))
f(head, 2)


# dry run this code in a notebook and you'll understand the code
# it's easy once you understand it
def neetcode_approach(head, k):
    dummy = Node(0, head)
    groupPrev = dummy

    def get_kth(prevNode, k):
        while prevNode and k > 0:
            prevNode = prevNode.next
            k -= 1
        return prevNode

    while True:
        kth = get_kth(groupPrev, k)
        if not kth:
            break
        groupNext = kth.next

        prev, curr = groupNext, groupPrev.next  # why we took prev = groupNext ? dry run and see for yourself
        while curr != groupNext:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        tmp = groupPrev.next
        groupPrev.next = kth
        groupPrev = tmp
    
    return dummy.next

head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8))))))))
neetcode_approach(head, 3)


def striver_approach(head, k):
    if not head or k == 1: return head

    dummy = Node(0, head)
    # count no of nodes in the LL
    count = 0
    pre, cur = dummy, dummy
    while cur.next: # while cur.next != null
        cur = cur.next
        count += 1
    
    while count >= k:
        cur = pre.next
        nex = cur.next
        for i in range(k-1):
            cur.next = nex.next
            nex.next = pre.next
            pre.next = nex
            nex = cur.next
        pre = cur
        count -= k
    
    return dummy.next

head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8))))))))
striver_approach(head, 3)