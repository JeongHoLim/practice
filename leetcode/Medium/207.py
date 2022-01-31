# 207. Course Schedule

class List(list): pass
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for a,b in prerequisites:
            graph[a].append(b)

        history = set()
        def dfs(idx):
            history.add(idx)
            for t in graph[idx]:
                if t in history:
                    return False
                if not dfs(t):
                    return False 
            history.remove(idx)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

s = Solution()
numCourses = 4
prerequisites = [[0,1],[1,3],[3,2]]

print(s.canFinish(numCourses,prerequisites))