# LC: https://leetcode.com/problems/valid-palindrome/
# neetcode

import string


def validPalindrome(s):
    def isAlphaNumeric(char):
        return (char in string.ascii_letters or char in string.digits)

    l, r = 0, len(s) -1
    while l <= r:
        while l<r and not isAlphaNumeric(s[l]):
            l += 1
        while l<r and not isAlphaNumeric(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True

# note: l < r condition is important
# eg. s = " "
# if you run with this input, without l<r condition, it will throw index error: list index out of range
# even l <= r condition will throw an error
# note that strictly 'less than' condition is there due to l += 1 and r -= 1
# if l = r - 1, then due to l += 1, it will become l = r
# but if we kept while l <= r, then l would have become l = r + 1 and crossed the right pointer