# LC: https://leetcode.com/problems/rotate-list/
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743812259_42Unit

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
def rotate_list(head, k):
    if not head or not head.next or k == 0:
        return head

    # find length and last node
    length = 1
    last_node = head
    while last_node.next:
        last_node = last_node.next
        length += 1
    
    k %= length     # this is how many times we actually need to rotate
    skip_nodes = length - k

    # rewire: make proper connections
    last_node.next = head
    node_before_new_head = head
    i = 0
    while i < skip_nodes - 1:
        node_before_new_head = node_before_new_head.next
        i += 1
    head = node_before_new_head.next
    node_before_new_head.next = None

    return head

rotate_list(Node(1, Node(2, Node(3, Node(4, Node(5, Node(6)))))), 3)