# https://programmers.co.kr/learn/courses/30/lessons/49191?language=python3

from collections import defaultdict,deque
def solution(n, results):
    answer = 0
    graph = defaultdict(list)
    win = [0]+[set() for _ in range(n)]
    lose = [0]+[set() for _ in range(n)]
    for i in range(1,n+1):
        graph[i].extend([])
    
    for a,b in results:
        graph[a].append(b)
        win[a].add(b)
        lose[b].add(a)
    
    for f,s in graph.items():
        queue = deque([f])
        visited = []
        while queue:
            v = queue.popleft()
            win[f] |= win[v]
            lose[v] |= lose[f]
            for t in graph[v]:
                if t not in visited:
                    queue.append(t)
                    visited.append(t)
    
    for i in range(1,n+1):
        if len(win[i]) + len(lose[i]) == n-1: answer += 1
    
    return answer