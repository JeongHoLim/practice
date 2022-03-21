class List(list): pass

from collections import defaultdict,deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append([v,w])

        queue = deque([[k,0]])
        visited = set([k])
        answer = float('-inf')
        while queue:
            cur_node = queue.popleft()
            
            for v,w in graph[cur_node[0]]:
                if v not in visited:
                    visited.add(v)
                    queue.append([v,w+cur_node[1]])
            answer = max(answer,cur_node[1])
        
        if len(visited) != n:
            return -1
        return answer        




s = Solution()
times = [[1,2,1],[2,3,2],[1,3,4]]

n = 3
k = 1


print(s.networkDelayTime(times,n,k))