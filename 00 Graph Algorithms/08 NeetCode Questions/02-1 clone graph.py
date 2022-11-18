# problem: https://leetcode.com/problems/clone-graph/
# sol: https://leetcode.com/problems/clone-graph/discuss/1792858/Python3-ITERATIVE-BFS-(beats-98)-'less()greater''-Explained
# exaplanation: https://www.youtube.com/watch?v=xZ9st62u2Yk

# why add neighbours saperately in the first place?
# Why do the neighbour's need to be added separately? Why can't we add clones to the dict with: Node(n.val, n.neighbors)
# This causes the clones to be references to the original and not copies


from collections import deque


class Node:
    def __init__(self, val=0, neis=[]):
        self.val = val
        self.neis = neis

# if you don't understand the code, dry run by yourself
# neetcode taught that you can put simply everything in python dictionaries
def f(node):
    if not node: return None

    queue = deque()
    queue.append(node)
    clone = {node: Node(node.val, [])}  # similar to set() visited
    while queue:
        deNode = queue.popleft()
        for nei in deNode.neis:
            if nei not in clone:    # if nei not in visited
                clone[nei] = Node(nei.val)
                queue.append(nei)
            clone[deNode].neis.append(clone[nei])
    return clone[node]


# neetcode solution
def f(node):
    oldToNew = {}   # original node: copy node

    def dfs(node):
        # if copy already exists in the hashmap, return it otherwise create one
        if node in oldToNew:
            return oldToNew[node]
        copy = Node(node.val)
        oldToNew[node] = copy

        for nei in node.neighbours:
            copy.neighbours.append(dfs(nei))
        return copy
    
    return dfs(node) if node else None


