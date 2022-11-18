# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743796880_40Unit
# also reverse the groups with len(group) < k

class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next


def f(head, k):
    if k == 1: return head

    dummy = Node(0, head)
    prev, cur = dummy, head
    while True:
        # we'll need these two pointers in future
        end_prev = prev
        start_cur = cur

        # find next group start
        i = 0
        start_next = cur
        while start_next and i < k:
            start_next = start_next.next
            i += 1
        
        # reverse this group
        prev, cur = start_next, start_cur
        i = 0
        while cur and i < k:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            i += 1
        
        # connect
        end_prev.next = prev

        # update
        prev = start_cur    # since start_cur is now the last node of the group
        # no need to update cur since it is already at start of the next group now

        # break the loop
        if not cur: break

    return dummy.next

f(Node(1, Node(2)), 2)
f(Node(1, Node(2, Node(3, Node(4, Node(5))))), 3)


def reverse_every_k_elements(head, k):
    if k <= 1 or head is None:
        return head
    
    prev, curr = None, head
    while True:
        end_prev = prev     # last node of the previous group
        start_sub = curr

        # reverse k-group
        i = 0
        while curr and i < k:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            i += 1
        
        # connect with the previous part
        if end_prev:    # if end node of prev group is not none ie. if it is not the first group
            end_prev.next = prev    # since prev is now the head of reversed LL
        else:
            head = prev
        
        # connect with the next part
        start_sub.next = curr   # since start_sub is now the last node of the sub list

        if not curr:
            break
        prev = start_sub
    
    return head

reverse_every_k_elements(Node(1, Node(2)), 2)
reverse_every_k_elements(Node(1, Node(2, Node(3, Node(4, Node(5))))), 3)