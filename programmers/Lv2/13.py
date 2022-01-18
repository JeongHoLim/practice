# https://programmers.co.kr/learn/courses/30/lessons/72411?language=python3#

from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []
    history = defaultdict(int)
    for order in map(sorted,orders):
        for c in course:
            for combo in map("".join,combinations(order,c)):
                history[combo] += 1
    
    candidates = sorted(history.items(),key=lambda x : x[1],reverse=True)
    count = [0]*11
    for candidate in candidates:
        if candidate[1] == 1 or candidate[1] < count[len(candidate[0])]:
            continue
        count[len(candidate[0])] = candidate[1]
        answer.append(candidate[0])
    
    answer.sort()
    return answer