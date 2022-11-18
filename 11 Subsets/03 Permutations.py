# LC: https://leetcode.com/problems/permutations/
# grokking: https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628744061506_69Unit

# see grokking article to understand both the code

from collections import deque

# bfs
def find_permutations(nums):
    numsLength = len(nums)
    result = []
    permutations = deque()
    permutations.append([])
    for currentNumber in nums:
        # we will take all existing permutations and add the current number to create 
        # new permutations
        n = len(permutations)
        for _ in range(n):
            oldPermutation = permutations.popleft()
            # create a new permutation by adding the current number at every position
            for j in range(len(oldPermutation)+1):
                newPermutation = list(oldPermutation)
                newPermutation.insert(j, currentNumber)
                if len(newPermutation) == numsLength:
                    result.append(newPermutation)
                else:
                    permutations.append(newPermutation)

    return result

print(find_permutations([1,2,3]))

# dfs
def generate_permutations(nums):
    result = []
    def dfs(index, currentPermutation, result):
        if index == len(nums):
            result.append(currentPermutation)
        else:
            # create a new permutation by adding the current number at every position
            for i in range(len(currentPermutation)+1):
                newPermutation = list(currentPermutation)
                newPermutation.insert(i, nums[index])
                dfs(index + 1, newPermutation, result)
    dfs(0, [], result)
    return result

print(generate_permutations([1,2,3]))

# time: O(n*n!)
# space: O(n*n!)
# go to grokking to understand