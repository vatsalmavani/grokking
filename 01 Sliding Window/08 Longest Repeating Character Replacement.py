# leetcode: https://leetcode.com/problems/longest-repeating-character-replacement/
# neetcode: https://www.youtube.com/watch?v=gqXU1UyA8pk
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628541037657_4Unit

def charReplacement(s, k): # s = string
    count = {}
    result = 0
    
    l = 0
    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1

        while (r - l + 1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1
        
        result = max(result, r-l+1)
    return result