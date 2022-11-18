# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743804225_41Unit


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def f(head, k):
    dummy = Node(0, head)
    prev, curr = dummy, head
    while True:     # or while curr
        end_prev = prev
        start_curr = curr

        i = 0
        start_next = start_curr
        while start_next and i < k:
            start_next = start_next.next
            i += 1
        
        i = 0
        prev, curr = start_next, start_curr
        while curr and i < k:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            i += 1

        end_prev.next = prev

        i = 0
        while curr and i < k:
            prev = curr
            curr = curr.next
            i += 1

        if not curr: break
    
    return dummy.next

head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8))))))))
f(head, 2)


def reverse_alternate_k_elements(head, k):
    if k <= 1 or head is None:
        return head
    
    current, previous = head, None
    while current is not None: # break if we've reached the end of the list
        last_node_of_previous_part = previous
        # after reversing the LinkedList 'current' will become the last node of the sub-list
        last_node_of_sub_list = current

        # reverse 'k' nodes
        i = 0
        while current is not None and i < k:
            next = current.next
            current.next = previous
            previous = current
            current = next
            i += 1

        # connect with the previous part
        if last_node_of_previous_part is not None:
            last_node_of_previous_part.next = previous
        else:
            head = previous

        # connect with the next part
        last_node_of_sub_list.next = current

        # skip 'k' nodes
        i = 0
        while current is not None and i < k:
            previous = current
            current = current.next
            i += 1

    return head

head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8))))))))
reverse_alternate_k_elements(head, 3)
reverse_alternate_k_elements(head, 2)

# O(n) time and O(1) space