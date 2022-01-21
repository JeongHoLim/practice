# https://programmers.co.kr/learn/courses/30/lessons/49189?language=python3

from collections import defaultdict,deque
def solution(n, edges):
    
    def bfs(graph,n):
        queue = deque()
        queue.append(1)        
        visited = [-1]*(n+1)
        visited[1] = 0
        
        while queue:
            node = queue.popleft()
            for v in graph[node]:
                if visited[v] == -1:
                    queue.append(v)
                    visited[v] = visited[node]+1 
            
        return visited.count(max(visited))
    
    graph = defaultdict(list)
    
    for f,t in edges:
        graph[f].append(t)
        graph[t].append(f)
    
    return bfs(graph,n)