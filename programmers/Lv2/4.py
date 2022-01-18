
# https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3

from collections import deque

def solution(progresses, speeds):
    answer = []
    
    bepo = 0
    
    queue = deque(map(sum,zip(progresses,speeds)))

    while True:
        while len(queue) > 0 and queue[0] >= 100:
            bepo += 1
            queue.popleft()
            speeds.pop(0)
        if bepo>0:
            answer.append(bepo)
            bepo = 0
        elif len(queue) > 0:
            for i in range(len(queue)):
                queue[i] += speeds[i]
        else: break
            
    return answer