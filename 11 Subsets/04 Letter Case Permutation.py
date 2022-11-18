# LC: https://leetcode.com/problems/letter-case-permutation/
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628744066603_70Unit

# understand from grokking and python tutor

def find_letter_case_string_permutations(str):
    permutations = []
    permutations.append(str)
    # process every character of the string one by one
    for i in range(len(str)):
        if str[i].isalpha():  # only process characters, skip digits
            # we will take all existing permutations and change the letter case appropriately
            n = len(permutations)
            for j in range(n):
                chs = list(permutations[j])
                # if the current char is in upper case, change it to lower case or vice versa
                chs[i] = chs[i].swapcase()
                permutations.append(''.join(chs))

    return permutations

print(find_letter_case_string_permutations("a4b2"))

# time: O(n*n^2)
# space: O(n*n^2)\
# understand from grokking