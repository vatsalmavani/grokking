# https://leetcode.com/problems/course-schedule/

'''
this problem can be solved in 2 ways:
    1. topological sort
    2. detecting a cycle
note: neetcode's solution is just DFS alternative to kahn's algo
'''

# topo sort solution:
class Solution:
    def canFinish(self, numCourses: int, prereq: list[list[int]]) -> bool:
        
        if not prereq:
            return True
        
        graph = {}
        indegree = {}
        for i in range(numCourses):
            graph[i] = []
            indegree[i] = 0
        for u,v in prereq:
            graph[v].append(u)
            indegree[u] += 1
        def kahn():
            queue = []
            visited = []
            for k,v in indegree.items():
                if v == 0:
                    queue.append(k)
                    visited.append(k)
            while queue:
                deVertex = queue.pop(0)
                for child in graph[deVertex]:
                    if child not in visited:
                        indegree[child] -= 1
                        if indegree[child] == 0:
                            queue.append(child)
                            visited.append(child)
            if len(visited) == numCourses:
                return True
            else:
                return False
        
        return kahn()