# https://programmers.co.kr/learn/courses/30/lessons/42628?language=python3

import heapq
def solution(operations):
    
    min_heap = []
    max_heap = []
    
    for op in operations:
        o1,o2 = op.split(" ")
        if o1 == "I":
            heapq.heappush(min_heap,int(o2))
            heapq.heappush(max_heap,-int(o2))
        elif min_heap:
            if o2 =="1":
                pop = heapq.heappop(max_heap)
                min_heap.remove(-pop)
                heapq.heapify(min_heap)
            else:
                pop = heapq.heappop(min_heap)
                max_heap.remove(-pop)
                heapq.heapify(max_heap)
        
    if not min_heap:
        return [0,0]
    else:
        return [-heapq.heappop(max_heap),heapq.heappop(min_heap)]