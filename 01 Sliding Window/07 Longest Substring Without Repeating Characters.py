# explanation: https://www.youtube.com/watch?v=jHj13UHURr8
# leetcode: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# sol: https://youtu.be/wiGpQwVHdE0
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628541027921_3Unit

def longest_substring_with_distinct_chars(s: str):
    repeating = set()
    l = 0   # left pointer or window_start
    max_length = 0
    for r in range(len(s)):     # right pointer or window_end
        while s[r] in repeating:
            repeating.remove(s[l])
            l += 1
        repeating.add(s[r])
        max_length = max(max_length, r-l+1)
    return max_length

# using hash table

def longest_substring(s):
        maxlen = 0
        freq = {}
        l = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            
            while freq[s[r]] > 1:
                freq[s[l]] -= 1
                l += 1
            
            maxlen = max(maxlen, r-l+1)
            
        return maxlen