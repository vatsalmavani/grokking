# LC: https://leetcode.com/problems/happy-number/
# grokking (this code): https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743560700_15Unit
# neetcode has normal solution

# this is a problem of finding cycle and hence use fast and slow pointer method

def find_happy_number(num):
    slow, fast = num, num
    while True:
        slow = find_square_sum(slow)  # move one step
        fast = find_square_sum(find_square_sum(fast))  # move two steps
        if slow == fast:  # found the cycle
            break
    return slow == 1  # see if the cycle is stuck on the number '1'


def find_square_sum(num):
    _sum = 0
    while (num > 0):  # OR while num:     # means while nums != 0 (False)
        digit = num % 10
        _sum += digit ** 2
        num //= 10
    return _sum


def main():
    print(find_happy_number(23))
    print(find_happy_number(12))


main()

# calculating time complexity is complicated. you can see in grokking page how to calculate it
# time complexity is O(log(N)) where N is the number we want to find "is happy or not"
# space complexity is O(1)

# same code, slighty different
def happy(num):
    def squaresum(num):
        ss = 0
        while num != 0:
            digit = num % 10
            ss += digit**2
            num //= 10
        return ss
    
    slow = fast = num
    slow = squaresum(slow)
    fast = squaresum(squaresum(fast))
    while slow != fast:
        slow = squaresum(slow)
        fast = squaresum(squaresum(fast))
    
    if slow == 1: return True
    return False