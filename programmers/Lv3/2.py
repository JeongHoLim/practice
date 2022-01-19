# https://programmers.co.kr/learn/courses/30/lessons/42627#

import heapq
def solution(jobs):
    answer = 0
    jobs.sort()
    
    tick = 0
    temp_sum = 0
    tasks = []
    i = count = 0
    
    while count < len(jobs):
        while i < len(jobs):
            if jobs[i][0] <= tick:
                heapq.heappush(tasks,(jobs[i][1],jobs[i]))
                i += 1
            else: break
        
        if not tasks:
            tick = jobs[i][0]
            continue
        
        task = heapq.heappop(tasks)
        tick += task[1][1]
        temp_sum += tick-task[1][0]
        count += 1
        
    answer = temp_sum//len(jobs)
    return answer