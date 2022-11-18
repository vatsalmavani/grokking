# LC: https://leetcode.com/problems/backspace-string-compare/
# different approach solution (O(M^2 + N^2) time and O(M + N) space): https://www.youtube.com/watch?v=nxo_4FzXLxU
# grokking (O(M + N) time, O(1) space) (this code): https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743506829_10Unit
# understand approach 2 through this maybe: https://www.youtube.com/watch?v=MGOjHoeMlsM


def backspaceNaive(s,t):
    s_out, t_out = [], []
    
    for char in s:  # O(M)
        if char == '#':
            if s_out: s_out.pop()   # if s_out is non empty
        else:
            s_out.append(char)
    
    for char in t:  # O(N)
        if char == '#':
            if t_out: t_out.pop()
        else:
            t_out.append(char)
    
    return s_out == t_out     # The complexity of comparing two lists is O(n) if both lists have length n, and O(1) if the lists have different lengths.

# both time and space complexity are O(M + N)


#############################################################################


def backspace_compare(s,t):
    # use two pointer approach to compare the strings
    # going from back to beginning and checking for '#'
    i,j = len(s)-1, len(t)-1

    while i >= 0 or j >= 0:
        skipS, skipT = 0, 0

        # go to the next valid index in s
        while i >= 0:
            if s[i] == '#':
                skipS += 1
                i -= 1
            elif skipS > 0:
                skipS -= 1
                i -= 1
            else:
                break
        
        # go to the next valid index in t
        while j >= 0:
            if t[j] == '#':
                skipT += 1
                j -= 1
            elif skipT > 0:
                skipT -= 1
                j -= 1
            else:
                break
        
        if (i >= 0 and j < 0) or (j >= 0 and i < 0):
            # eg. "a#" and "a"
            return False
        
        # check if the chars of current valid index match
        if i >= 0 and j >= 0 and s[i] != t[j]:
            return False
        
        # since i and j are already checked, decreament them
        i -= 1
        j -= 1

    return True

print(backspace_compare("xy#z", "xzz#"))
print(backspace_compare("xy#z", "xyz#"))
print(backspace_compare("xp#", "xyz##"))
print(backspace_compare("xywrrmp", "xywrrmu#p"))

# O(M + N) time, O(1) space

def f(s,t):
    l,r = len(s)-1, len(t)-1
    scount, tcount = 0, 0
    while l >= 0 and r >= 0:
        while l >= 0 and s[l] == '#':
            scount += 1
            l -= 1
        while l >= 0 and scount > 0:
            scount -= 1
            l -= 1
        if l >= 0:
            schar = s[l]

        while r >= 0 and t[r] == '#':
            tcount += 1
            r -= 1
        while r >= 0 and tcount > 0:
            tcount -= 1
            r -= 1
        if r >= 0:
            tchar = t[r]

        if l >= 0 and r >= 0 and schar != tchar: return False
        if (l >= 0 and r < 0) or (l < 0 and r >= 0): return False
        l -= 1; r -= 1
    return True

print(f("a#", "#"))
print(f("###", "#"))
print(f("ab#c", "ad#c"))
print(f("abc#", "adc#"))