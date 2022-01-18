# https://programmers.co.kr/learn/courses/30/lessons/42747

import collections

def solution(citations):
    answer = 0
    sorted_citations = sorted(citations,reverse = True)

    answer = max(map(min, enumerate(sorted_citations, start=1)))
    
    return answer