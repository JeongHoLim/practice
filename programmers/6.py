
# https://programmers.co.kr/learn/courses/30/lessons/64065

import collections
def solution(s):
    answer = []
    parsed = sorted(list(map(lambda x : x.strip("{}"), s.split("},{"))),key=lambda x : len(x))
    check = collections.defaultdict(bool)
    
    for p in parsed:
        for x in p.split(","):
            if not check[x]: 
                check[x] = True
                answer.append(int(x))
        
    return answer