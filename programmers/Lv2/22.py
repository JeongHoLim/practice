# https://programmers.co.kr/learn/courses/30/lessons/42578?language=python3

from collections import defaultdict

def solution(clothes):

    my_dict = defaultdict(list)
    
    for c in clothes:
        my_dict[c[1]].append(c[0])
    ans = 1
    
    for k,v in my_dict.items():
        ans *= (len(v) + 1)
    
    return ans - 1