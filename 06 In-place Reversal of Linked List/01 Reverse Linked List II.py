# LC: https://leetcode.com/problems/reverse-linked-list-ii/
# approach 1 (ayushi sharma): https://youtu.be/tHKp8UuOkm4
# approach 2 (neetcode): https://youtu.be/RF_M9tX4Eag



# THIS CODE DOES NOT WORK IN EDGE CASES SO UPDATE IT
# edge cases: (there may be other edge cases)
# left = 0
# right = len(linked list) - 1
# left = 0 AND right = len(linked list) - 1
# left = right

class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next
    
def f(head, left, right):
    dummy = Node(0, head)
    curr = dummy
    i = 0
    while curr and i < left:
        prev = curr
        curr = curr.next
        i += 1
    end_prev = prev
    i = 0
    while curr and i < right - left + 1:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        i += 1
    end_prev.next.next = curr
    end_prev.next = prev
    return dummy.next

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
head = f(head, 1,1)
while head:
    print(head.val)
    head = head.next

#######################################################################
### MY CODE ###

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def f(head, l, r):
    if l == r: return head

    dummy = Node(0, head)

    # reach to left
    i = 1
    prev, cur = dummy, head
    while i < l:
        prev = cur
        cur = cur.next
        i += 1
    end_1st = prev
    l = cur

    # reach to right
    while i <= r:
        prev = cur
        cur = cur.next
        i += 1
    r = prev
    start_2nd = cur

    # reverse left to right
    r.next = None
    prev, cur = start_2nd, l
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur 
        cur = nxt

    # connect
    end_1st.next = r

    return dummy.next

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
f(head, 2,4)


#######################################################################


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


########## approach 1 ##########


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def f(head, left, right):
    if left == right: return head

    def reverse(head):
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
    # getting the start node of the sub list to be reversed
    curr, prev = head, None
    count = 1
    while count < left:
        prev = curr
        curr = curr.next
        count += 1
    start = curr

    # head of the second half
    while count < right:
        curr = curr.next
        count += 1
    rest = curr.next

    # curr.next is necessary to end the reversing at the last node of the sub list
    curr.next = None
    new_head = reverse(start)

    # if left == 1: prev will be none since the first while loop didn't execute
    if prev is not None:
        prev.next = new_head

    # going to the last node of the sub list to connect it with the second half
    curr = new_head
    while curr.next is not None:
        curr = curr.next
    curr.next = rest
    
    if left == 1:
        return new_head
    else:
        return head

f(Node(3, Node(5)), 1,2)
f(Node(1, Node(2, Node(3, Node(4, Node(5))))), 2, 4)
f(Node(1, Node(2, Node(3, Node(4, Node(5, Node(6)))))), 3, 4)


##### same approach, modified code according to my understanding #####


def f(head, l, r):
    if l == r: return head
    
    # reach to left
    prev, curr = None, head
    i = 1
    while i < l:
        prev = curr
        curr = curr.next
        i += 1
    
    # if l == 1 then prev = None. In that case, end of 1st half is head itself
    if not prev:
        end_1st = head
    else:
        end_1st = prev
    start_sub = curr

    # save start of 2nd half for future
    while i < r:
        curr = curr.next
        i += 1
    start_2nd = curr.next

    # reverse the sub list
    i = l
    prev, curr = None, start_sub
    while i <= r:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        i += 1
    head_sub = prev

    # join everything
    end_1st.next = head_sub
    start_sub.next = start_2nd

    return head if l != 1 else head_sub



########## approach 2 ##########


def f(head, left, right):
    dummy = Node(0, head)
    leftPrev, cur = dummy, head

    for i in range(left - 1):
        leftPrev, cur = cur, cur.next
    # leftPrev @ last node of first half
    # cur @ first node of the sub list

    # reverse the sub list
    prev = None
    for i in range(right - left + 1):
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    # prev @ last node (which is now first) of the sub list to which first half needs to be connected
    # cur @ head of the second half

    leftPrev.next.next = cur
    leftPrev.next = prev

    return dummy.next

f(Node(5), 1, 1)
f(Node(3, Node(5)), 1, 2)


##### same approach, modified code according to my understanding #####


def f(head, left, right):
    dummy = Node(0, head)
    
    prev, curr = dummy, head
    i = 1
    while i < left:
        prev = curr
        curr = curr.next
        i += 1
    end_1st = prev
    end_sub = curr

    prev = None
    while i <= right:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        i += 1
    start_sub = prev
    start_2nd = curr

    end_1st.next = start_sub
    end_sub.next = start_2nd

    return dummy.next