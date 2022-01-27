# https://programmers.co.kr/learn/courses/30/lessons/42890#

from collections import defaultdict
from itertools import combinations

def solution(relation):
    answer = 0
    my_dict = defaultdict(set)
    for entity in relation:
        for i,col in enumerate(entity):
            my_dict[i].add(col)
            
    pk = []
    npk = []
    n = len(relation)
    for k,v in my_dict.items():
        if len(v) != n: npk.append(k)
        else: pk.append(k)
    
    answer += len(pk)
    i = 2
    cdk = []
    while i <= len(npk):
        for x in combinations(npk,i):
            flg = True
            for k in cdk:
                if sum(1 for tx in x if tx in k) == len(k):
                    flg = False
                    break
            if not flg: continue
            for j in range(n):
                key = "".join(relation[j][k] for k in x)
                my_dict[x].add(key)
            if len(my_dict[x]) == n:
                answer += 1
                cdk.append(x)
        i += 1
    return answer