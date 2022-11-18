# leetcode: https://leetcode.com/problems/find-all-anagrams-in-a-string/
# neetcode: https://www.youtube.com/watch?v=G8xtZy0fDKg

# same as previous problem

import string


def findAnagrams(s, p):     # s = string; p = pattern
    hs = dict.fromkeys(string.ascii_lowercase, 0)   # hashmap for string
    hp = dict.fromkeys(string.ascii_lowercase, 0)   # hashmap for pattern

    for i in p:
        hp[i] += 1
    
    l = 0
    res = []    # result
    for r in range(len(s)):
        hs[s[r]] += 1
        
        if r-l+1 > len(p):
            hs[s[l]] -= 1
            l += 1
        
        matches = 0
        for char in string.ascii_lowercase:
            if hs[char] == hp[char]:
                matches += 1
        
        if matches == 26:
            res.append(l)
    
    return res

# time complexity: O(26*n); n = len(s)

##############################################################################


from typing import Counter


def f(s, p):
    l = 0
    char_freq = Counter(p)
    matches = 0
    res = []
    for r in range(len(s)):
        # add right pointer char
        if s[r] in char_freq:
            char_freq[s[r]] -= 1
            if char_freq[s[r]] == 0:
                matches += 1
        
        # remove left pointer char
        if r-l+1 > len(p):
            if s[l] in char_freq:
                if char_freq[s[l]] == 0:
                    matches -= 1
                char_freq[s[l]] += 1
            l += 1

        if matches == len(char_freq):
            res.append(l)
    
    return res

# time complexity: O(p); p = len(p)
# space complexity: O(p); due to dictionary - char_freq

print(f("cbasdbaccciab", "abc"))
print(f("baa", "aa"))