# https://programmers.co.kr/learn/courses/30/lessons/72412?language=python3

import collections
import bisect
import itertools

def solution(info, queries):
    answer = []
    default_val=[
    ["java","python","cpp"],
    ["backend","frontend"],
    ["junior","senior"],
    ["chicken","pizza"]
    ]
        
        
    def push(combi,my_dict,l,p,c,f,s):
        my_dict[(l,p,c,f)].append(s)       
            
        for cm in combi:
            for t in list(cm):
                copy = [l,p,c,f]
                for i in t:
                    copy[i] = '-'
                my_dict[tuple(copy)].append(s)
     
    combinations = []
    examples = [0,1,2,3]
    
    for i in range(1,5):
        combinations.append(list(itertools.combinations(examples,i)))
    
    my_dict = collections.defaultdict(list)
    
    
    for x in info:
        l,p,c,f,s = x.split()
        push(combinations,my_dict,l,p,c,f,int(s))
    
    for x in my_dict.items():
        x[1].sort()
        
    for query in queries:
        l,p,c,fs = map(str.strip,query.split('and'))
        f,s = fs.split()
        s = int(s)
        t = my_dict[l,p,c,f]
        answer.append(len(t) - bisect.bisect_left(t,s))
        
    
    return answer