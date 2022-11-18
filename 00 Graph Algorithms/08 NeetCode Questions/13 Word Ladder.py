# LC: https://leetcode.com/problems/word-ladder/
# NC: https://youtu.be/h9iTnkgv05E
# watch neetcode's explanation to understand why graph and why bfs

from collections import deque
import string


def ladderLength(beginWord, endWord, wordList):
    queue = [(beginWord, 1)]
    visited = set()     # no need to add beginWord in visited bcoz it is not in the wordList
    
    while queue:
        word, dist = queue.pop(0)
        if word == endWord:
            return dist
        for i in range(len(word)):
            for j in 'abcdefghijklmnopqrstuvwxyz':
                tmp = word[:i] + j + word[i+1:]
                # note that these two for loops makes tmp a neighbour of word
                # hence, basically it is still a normal bfs
                # just the way of retrieving the neighbour is different based on the problem
                if tmp not in visited and tmp in wordList:
                    queue.append((tmp, dist+1))
                    visited.add(tmp)
    return 0

######################################################################
# to optimize it, we need few tweaks:

def ladderLength(beginWord, endWord, wordList):
    if endWord not in wordList: return 0    # this line decreases time taken
    # the below code would also return 0 but if the endWord is not in the wordList, we don't need to go through the code

    queue = deque([(beginWord, 1)])
    visited = set()     # no need to add beginWord in visited bcoz it is not in the wordList
    wordList = set(wordList)    # hashSet is faster than array
    
    while queue:
        word, dist = queue.popleft()
        if word == endWord:
            return dist
        for i in range(len(word)):
            for j in string.ascii_lowercase:    # faster than 'abc...xyz'
                tmp = word[:i] + j + word[i+1:]
                # note that these two for loops makes tmp a neighbour of word
                # hence, basically it is still a normal bfs
                # just the way of retrieving the neighbour is different based on the problem
                if tmp not in visited and tmp in wordList:
                    queue.append((tmp, dist+1))
                    visited.add(tmp)
    return 0
    # time complexity of bfs algorithm is O(V + E); v = no of vertex; e = no of edges
    # here, total nodes are len(wordList) - l - and each node can have w*26 edges (w = len(word))
    # hence, time complexity = O(wl) but creating tmp, parsing the word also takes O(len(word)) time
    # hence, final TC = O(w^2 *l)

# in the queue.append((tmp, dist+1)), note that distance itself is not changing
# just we are adding 1 to distance
# run this code on python tutor if you don't understand the dist part and why this is stil a bfs on graph even if we didn't explicitely create a graph hash table

wordlist = ['abc','abf','adc','aec','eef','def','dbf','ebf','dec']
start = 'abc'
end = 'def'

print(ladderLength(start, end, wordlist))


# intuitive code that gives TLE:
# TLE is leetcode's problem, not ours (this code passes 33 tests out of 50 and then gives TLE)
# hence, this approach is perfectly fine
from collections import defaultdict, deque
from string import ascii_lowercase


def f(beginWord, endWord, wordList):
    if endWord not in wordList: return 0
    wordList.append(beginWord)

    # create graph
    graph = defaultdict(list)
    for word in wordList:       # ----------------------> O(l); l = len(wordlist)
        vis = set([word])
        for i in range(len(beginWord)):     # ----------> O(w); w = len(word)
            for char in ascii_lowercase:    # ----------> O(26)
                temp = word[:i] + char + word[i+1:] # --> O(w) since parsing a string takes O(n) time where n = len(string)
                if temp not in vis and temp in wordList:
                    graph[word].append(temp)
                    vis.add(temp)
    # hence, total time complexity = O(w^2 *l)

    # bfs for sssp
    q = deque([[beginWord, 1]])
    visited = set([beginWord])
    while q:
        node, dist = q.popleft()
        if node == endWord:
            return dist
        for child in graph[node]:
            if child not in visited:
                q.append([child, dist + 1])
                visited.add(child)
    return 0

print(f("hit", "cog", ["hot","dot","dog","lot","log","cog"]))

# ls = "hot"	"dot"	"dog"	"lot"	"log"	"cog"	"hit"

# {'hot': ['dot', 'lot', 'hit'],
#  'dot': ['hot', 'lot', 'dog'],
#  'dog': ['cog', 'log', 'dot'],
#  'lot': ['dot', 'hot', 'log'],
#  'log': ['lot', 'dog', 'cog'],
#  'cog': ['dog', 'log'],
#  'hit': ['hot']}

# second way to create same graph
def f(begin, end, ls):
    if end not in ls: return 0
    ls.append(begin)
    graph = defaultdict(list)
    for word in ls:
        for i in range(len(word)):
            for char in ascii_lowercase:
                tmp = word[:i] + char + word[i+1:]
                if tmp in ls and tmp != word:
                    graph[word].append(tmp)
    return graph