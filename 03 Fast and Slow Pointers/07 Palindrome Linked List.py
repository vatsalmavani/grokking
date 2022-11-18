# LC: https://leetcode.com/problems/palindrome-linked-list/
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743582805_17Unit
# neetcode: https://youtu.be/yOzXms1J6Nk


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# approach 1: convert linked list to array and check if array is palindrome or not
# O(n) time and O(n) space
def arrayPalindrome(head):
    # convert LL to array
    nums = []
    while head:
        nums.append(head.val)
        head = head.next
    
    # check if array is palindrome?
    l,r = 0, len(nums)-1
    while l <= r:
        if nums[l] != nums[r]:
            return False
        l += 1
        r -= 1
    return True


# approach 2: reverse the 2nd half of linked list and check for palindrome
# O(n) time and O(1) space
def LLPalindrome(head: Node):
    if not head or not head.next:   # if head is none or there's only one node, it's palindrome
        return True
    
    # find middle of linked list (slow)
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # reverse the second half
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt

    # check palindrome
    left, right = head, prev
    while right: # or while left OR right: doesn't matter
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True


# "don't change the given linked list" - grokking
def is_palindromic_linked_list(head):
  if head is None or head.next is None:
    return True

  # find middle of the LinkedList
  slow, fast = head, head
  while (fast is not None and fast.next is not None):
    slow = slow.next
    fast = fast.next.next

  head_second_half = reverse(slow)  # reverse the second half
  # store the head of reversed part to revert back later
  copy_head_second_half = head_second_half

  # compare the first and the second half
  while (head is not None and head_second_half is not None):
    if head.value != head_second_half.value:
      break  # not a palindrome

    head = head.next
    head_second_half = head_second_half.next

  reverse(copy_head_second_half)  # revert the reverse of the second half

  if head is None or head_second_half is None:  # if both halves match
    return True

  return False


def reverse(head):
  prev = None
  while (head is not None):
    next = head.next
    head.next = prev
    prev = head
    head = next
  return prev


def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)

  print("Is palindrome: " + str(is_palindromic_linked_list(head)))

  head.next.next.next.next.next = Node(2)
  print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()