# leetcode: https://leetcode.com/problems/permutation-in-string/
# leetcode solution: https://leetcode.com/problems/permutation-in-string/discuss/2221058/Python-Sliding-Window-Time-O(N-%2B-M)-or-Space-O(1)-Explained

# understand logic from neetcode for O(26*n) time complexity

# is permutation of s1 in s2?

import string


def checkInclusion(s1, s2):
    hashmap1 = dict.fromkeys(string.ascii_lowercase, 0)
    hashmap2 = dict.fromkeys(string.ascii_lowercase, 0)

    for i in s1:
        hashmap1[i] += 1
    
    l = 0
    for r in range(len(s2)):
        hashmap2[s2[r]] += 1

        if r-l+1 > len(s1):  # while window size is greater than it should be, increase left pointer  # we can put if instead of while here
            hashmap2[s2[l]] -= 1
            l += 1
        
        matches = 0
        for ch in string.ascii_lowercase:
            if hashmap1[ch] == hashmap2[ch]:
                matches += 1
        
        if matches == 26:   # since english lower case letters are 26
            return True
    
    return False

s1 = "abc"; s2 = "oidbcaf"
print(checkInclusion(s1,s2))
s1 = "dc"; s2 = "odicf"
print(checkInclusion(s1,s2))
s1 = "bcdyabcdx"; s2 = "bcdxabcdy"
print(checkInclusion(s1,s2))
s1 = "abc"; s2 = "aaacb"
print(checkInclusion(s1,s2))

# time complexity is O(26*N)
# space complexity is O(26*2) = O(1) for 2 hashmaps



########################################################################

# approach 2: using matches variable (grokking method in 'find anagrams' problem (next problem))

from typing import Counter


def f(s,t):
    hs = Counter(s)
    l = 0
    matches = 0
    for r in range(len(t)):
        if t[r] in hs:
            hs[t[r]] -= 1
            if hs[t[r]] == 0:
                matches += 1
            
        if r-l+1 > len(s):
            if t[l] in hs:
                if hs[t[l]] == 0:
                    matches -= 1
                hs[t[l]] += 1
            l += 1
        
        if matches == len(hs): return True
    return False



########################################################################

# approach 3: neetcode using matches variable

def f(s1, s2):
    if len(s1) > len(s2): return False

    h1, h2 = dict.fromkeys(string.ascii_lowercase, 0), dict.fromkeys(string.ascii_lowercase, 0)
    matches = 0
    for char in s1:
        h1[char] += 1
    for i in range(len(s1)):
        h2[s2[i]] += 1
    for char in string.ascii_lowercase:
        if h1[char] == h2[char]:
            matches += 1
    if matches == 26: return True

    l = 0
    for r in range(len(s1), len(s2)):
        h2[s2[r]] += 1
        if h1[s2[r]] == h2[s2[r]]:
            matches += 1
        elif h2[s2[r]] == h1[s2[r]] + 1:
            matches -= 1

        if r-l+1 > len(s1): # this is always going to be true since we already made our window size equal to len(s1) before the for loop. so you can ditch this condition
            h2[s2[l]] -= 1
            if h1[s2[l]] == h2[s2[l]]:
                matches += 1
            elif h2[s2[l]] == h1[s2[l]] - 1:
                matches -= 1
            l += 1
        if matches == 26: return True
    return False

s1 = "ab"; s2 = "eidbaooo"
print(f(s1, s2))
s1 = "ab"; s2 = "eidbnaooo"
print(f(s1, s2))


# my version of neetcode solution:
from typing import Counter


def f(s,t):
    hs = Counter(s)
    ht = {}
    matches = 0
    l = 0
    for r in range(len(t)):
        # add right elements
        ht[t[r]] = ht.get(t[r], 0) + 1
        if t[r] in hs and ht[t[r]] == hs[t[r]]:
            matches += 1
        elif t[r] in hs and ht[t[r]] == hs[t[r]] + 1:
            matches -= 1
        # remove left elements
        if r-l+1 > len(s):
            if t[l] in hs and ht[t[l]] == hs[t[l]]:
                matches -= 1
            elif t[l] in hs and ht[t[l]] == hs[t[l]] + 1:
                matches += 1
            ht[t[l]] -= 1
            l += 1
        if matches == len(hs): return True
    return False