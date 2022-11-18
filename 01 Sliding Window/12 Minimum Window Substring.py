# leetcode: https://leetcode.com/problems/minimum-window-substring/
# neetcode (this code): https://youtu.be/jSto0O4AJbM
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628541068682_8Unit
# leetcode solution (this code): https://leetcode.com/problems/minimum-window-substring/solution/

# s = ""
# if not s:
#     print("s is empty string")


from typing import Counter

# s = "abca"
# hs = Counter(s)
# print(hs)

# l = [1,1,2,3,4,3,3,3,2]
# h = Counter(l)
# print(h)

def minWindow(s, t):    # s = string, t = pattern
    if not s or not t or len(t) > len(s):
        return ""
    
    window_counts, required = {}, Counter(t)     # hashmap s; hashmap t
    # result = window length, left pointer, right pointer
    result = float('inf'), None, None

    matches = 0
    l = 0
    for r in range(len(s)):
        right_char = s[r]
        window_counts[right_char] = window_counts.get(right_char, 0) + 1
        
        if right_char in required and window_counts[right_char] == required[right_char]:
            matches += 1
        
        while matches == len(required):
            left_char = s[l]
            if r-l+1 < result[0]:
                result = ((r-l+1), l, r)
            if left_char in required and window_counts[left_char] == required[left_char]:
                matches -= 1
            window_counts[left_char] -= 1
            l += 1
    
    return "" if result[0] == float('inf') else s[result[1]:result[2]+1]