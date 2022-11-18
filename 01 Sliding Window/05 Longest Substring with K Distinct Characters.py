# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628541009794_1Unit


def longest_substring_with_k_dist_char(word, k):
    window_start = 0
    max_length = 0
    char_freq = {}

    for window_end in range(len(word)):
        end_char = word[window_end]
        if end_char not in char_freq:
            char_freq[end_char] = 0
        char_freq[end_char] += 1

        while len(char_freq) > k:
            start_char = word[window_start]
            char_freq[start_char] -= 1
            if char_freq[start_char] == 0:
                del char_freq[start_char]
            window_start += 1
        
        max_length = max(max_length, window_end - window_start + 1)
    
    return max_length

print(longest_substring_with_k_dist_char("araaci", 2))
print(longest_substring_with_k_dist_char("araaci", 1))
print(longest_substring_with_k_dist_char("cbbebi", 3))

# same code but shorter

def findLength(s, k):
    visited = {}
    length = 0
    l = 0
    for r in range(len(s)):
        visited[s[r]] = visited.get(s[r], 0) + 1
        while len(visited) > k:
            visited[s[l]] -= 1
            if visited[s[l]] == 0:
                del visited[s[l]]
            l += 1
        length = max(length, r-l+1)
    return length

print(findLength("araaci", 2))
print(findLength("araaci", 1))
print(findLength("cbbebi", 3))