# LC: https://leetcode.com/problems/open-the-lock/
# neetcode: https://youtu.be/Pzg3bCDY87w

# almost similar to 'word ladder' problem

from collections import deque


def openLock(deadends, target):
    if "0000" in deadends: return -1

    def children(lock):
        res = []
        for i in range(4):
            res.append(lock[:i] + str((int(lock[i]) + 1) % 10) + lock[i+1:])
            res.append(lock[:i] + str((int(lock[i]) -1 + 10) % 10) + lock[i+1:])
        return res

    queue = deque()
    queue.append(["0000", 0])
    visited = set(deadends)
    visited.add("0000")
    while queue:
        lock, turns = queue.popleft()
        if lock == target:
            return turns
        for child in children(lock):
            if child not in visited:
                queue.append([child, turns + 1])
                visited.add(child)
    return -1