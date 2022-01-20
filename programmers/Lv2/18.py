# https://programmers.co.kr/learn/courses/30/lessons/42587?language=python3

import heapq
import collections

def solution(priorities, location):
    answer = 0
    
    heap = []
    queue = collections.deque()
    
    for i,p in enumerate(priorities):
        queue.append((-p,i))
        heapq.heappush(heap,-p)
    
    while queue:
        J = queue.popleft()
        if heap[0] < J[0]:
            queue.append(J)
            continue
            
        answer += 1
        heapq.heappop(heap)
        if J[1] == location:
            break
    return answer