# LC: https://leetcode.com/problems/circular-array-loop/
# grokking (this code explained nicely): https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743595805_19Unit
# use modulo operator for cylcles: https://realpython.com/python-modulo-operator/#how-to-create-cyclic-iteration


'''
i = 0
j = 0
while j <= 20:
    print(i)
    i = (i + 1) % 5     # 0,1,2,3,4,0,1,2,3,4,0...
    j += 1

i = 0
j = 0
while j <= 20:
    print(i)
    i = (i - 1) % 5     # 0,4,3,2,1,0,4,3,2,1,0...
    j += 1
'''


# there are three codes with decreasing time and space complexities
# go through them all while revising to know the approach



##### O(n^2) time and O(1) space #####
# time is O(n^2) bcoz we are iterating over each element trying to find cycle (and hence iterating again)
def is_cycle_present(nums):
    for i in range(len(nums)):
        is_forward = nums[i] > 0    # since non zero integers, is_forward is not nums[i] >= 0
        slow, fast = i,i
        
        # you can define a function outside the for loop, though, time comp won't change
        def find_next_index(cur_index, is_forward):
            direction = nums[cur_index] > 0
            if is_forward != direction:
                return -1
            next_index = (cur_index + nums[cur_index]) % len(nums)  # no need to put abs before (cur_index + nums[cur_index]). even if it is -ve (due to nums[cur_index]), % operator would make it +ve
            if cur_index == next_index:
                return -1
            return next_index

        while True:
            slow = find_next_index(slow, is_forward)
            fast = find_next_index(fast, is_forward)
            if fast != -1:
                fast = find_next_index(fast, is_forward)
            if slow == -1 or fast == -1 or slow == fast:    # fast can be -1 too. for example: [1,2]. fast starts at 1 and then when fast moves again, it reaches cycle 2 -> 2 -> 2...
                break
        
        if slow != -1 and slow == fast:     # here, you can put fast != -1 condition as well joined by 'and' but there is no need to since we are already checking slow == fast and slow != -1 so if both are true then of course fast != -1 is True as well
            return True
    
    return False

# you can visualise this in python tutor
print(is_cycle_present([-1,-2]))





##### O(n) time and O(n) space #####
# there is also a way to solve this problem in O(n) time and O(1) space by converting visited array indices to 0 but I can't figure out how to do that
def y(nums):
    def next_index(cur_index, is_forward):
        direction = nums[cur_index] > 0
        if direction != is_forward:
            return -1
        nextIndex = (cur_index + nums[cur_index]) % len(nums)
        if nextIndex == cur_index:
            return -1
        return nextIndex
    
    visited = set()
    for i in range(len(nums)):
        if i in visited:
            continue

        is_forward = nums[i] > 0
        slow, fast = i,i

        while True:
            slow = next_index(slow, is_forward)
            fast = next_index(fast, is_forward)
            if fast != -1:
                fast = next_index(fast, is_forward)
            visited.add(slow)
            visited.add(fast)
            if slow == -1 or fast == -1 or slow == fast:
                break
        
        if slow != -1 and slow == fast:
            return True
    return False
    
print(y([3,1,2]))



# code copied from the first comment: https://leetcode.com/problems/circular-array-loop/discuss/167525/python-1-pointer-O(n)-time-O(1)-space

##### O(n) time, O(1) space (by modifying input array) #####
# there is no way to keep existing array AND reduce space to O(1) we HAVE TO modify the array

def f(nums):
    for i,num in enumerate(nums):
        # use a distinct marker for each starting point
        mark = str(i)

        # explore while node is new, direction is same, and is not self loop
        # note: if node has been marked by a different marker, no need to proceed. This gives O(n) time.
        while type(nums[i]) == int and num*nums[i] > 0 and nums[i] % len(nums) != 0:
            jump = nums[i]
            nums[i] = mark
            i = (i + jump) % len(nums)

        # if self loop, nums[i] is never marked
        # if nums[i] is marked, a cycle is found
        if nums[i] == mark:
            return True
    return False

print(f([-1,-2]))
print(f([3,1,2]))

# note: keeping distinct 'marks' in one 'cycle' of for loop is imp
# see in python tutor what happens if you change mark to "same string for every iteration" or instead of mark variable, put just a 0
# visualize with this input: [-2,1,-1,-2,-2]