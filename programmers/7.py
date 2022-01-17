
# https://programmers.co.kr/learn/courses/30/lessons/42626?language=python3

import heapq
def solution(scoville, K):
    answer = 0
    heap = []
    
    heapq.heapify(scoville)
    
    while True:
        n1 = heapq.heappop(scoville)
        if n1 >= K: break
        elif len(scoville) == 0: 
            answer = -1
            break
        n2 = heapq.heappop(scoville)
        
        heapq.heappush(scoville,n1+n2*2)
        
        answer += 1
        
    return answer