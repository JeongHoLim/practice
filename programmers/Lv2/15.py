# https://programmers.co.kr/learn/courses/30/lessons/17677?language=python3

import re
from collections import defaultdict
def solution(str1, str2):
    answer = 0
    
    str1,str2 = str1.lower(),str2.lower()
    
    set1= defaultdict(int)
    set2= defaultdict(int)
    
    p = re.compile("[a-z]{2}")
    
    for i in range(len(str1)-1):
        if p.match(str1[i]+str1[i+1]):
            t = str1[i]+str1[i+1]
            set1[t] += 1
            
    for i in range(len(str2)-1):
        if p.match(str2[i]+str2[i+1]):
            t = str2[i]+str2[i+1]
            set2[t] += 1
    
    bm = bz = 0
    for x in set1.items():
        bm += max(x[1],set2[x[0]])
        bz += min(x[1],set2[x[0]])
    
    for x in set2.items():
        if x[0] not in set1.keys():
            bm += x[1]
    
    if bm == 0:
        answer = 65536
    else:
        answer = int((bz/bm)*65536)
    
    return answer