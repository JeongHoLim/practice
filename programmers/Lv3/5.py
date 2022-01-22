# https://programmers.co.kr/learn/courses/30/lessons/43162

from collections import defaultdict,deque

def solution(n, computers):
    answer = 0
     
    def bfs(graph,start,found):
        
        queue = deque()
        queue.append(start)
        visited = []
        while queue:
            f = queue.popleft()
            found.append(f)
            for t in graph[f]:
                if t not in visited:
                    queue.append(t)
                    visited.append(t)
    
    def get_answer(grpah):
        found = []
        ret = 0
        for k,v in graph.items():
            if len(v) == 1:
                ret += 1
                found.append(k)
                continue
            
            if k not in found:      
                bfs(graph,k,found)
                ret += 1
    
        return ret
    
    graph = defaultdict(list)
    
    for i,com in enumerate(computers):
        for ci,c in enumerate(com):
            if c == 1: graph[i].append(ci)
        
    answer = get_answer(graph)
    
    return answer