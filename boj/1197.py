from collections import defaultdict
import heapq



def func(graph,start,V):
    cost = 0
    candidate = []
    
    for w,f,t in graph[start]:
        heapq.heappush(candidate,(w,f,t))

    visited = set([start])
    while candidate:
        w,f,t = heapq.heappop(candidate)
        if t not in visited:
            visited.add(t)
            cost += w
            for w1,f1,t1 in graph[t]:
                if t1 not in visited:
                    heapq.heappush(candidate,(w1,f1,t1))
        

    return cost

graph = defaultdict(list)
V,E = list(map(int,input().split()))

for _ in range(E):
    A,B,C = list(map(int,input().split()))
    graph[A].append([C,A,B])
    graph[B].append([C,B,A])

print(func(graph,1,V))

