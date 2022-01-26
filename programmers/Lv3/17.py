# https://programmers.co.kr/learn/courses/30/lessons/42579

from collections import defaultdict
def solution(genres, plays):
    answer = []
    
    info = defaultdict(list)
    
    for i in range(len(genres)):
        info[genres[i]].append([plays[i],i])
    order = []
    for k in info.keys():
        info[k].sort(reverse=True,key=lambda x: (x[0],-x[1]))
        order.append([k,sum(map(lambda x:x[0],info[k]))])
    
    order.sort(reverse=True,key=lambda x : x[1])
    
    for o in order:
        answer.extend(map(lambda x : x[1],info[o[0]][:2]))
        
        
    return answer