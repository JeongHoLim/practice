# https://programmers.co.kr/learn/courses/30/lessons/77486?language=python3

from collections import defaultdict

def solution(enroll, referral, seller, amount):
    
    answer = [0]*len(enroll)
    
    info = defaultdict(int)
    tree = defaultdict(list)
    
    for i,people in enumerate(enroll):
        tree[i].append(people)
        info[people] = i    
    
    for i,people in enumerate(referral):
        if people == "-": continue
        tree[i].append(people)
    
    for i in range(len(seller)):
        earned,people = amount[i]*100,seller[i]
        while earned > 0:
            parent = tree[info[people]]
            answer[info[people]] += earned - earned//10
            if len(parent) == 1:
                break
            earned,people = earned//10,parent[1]

        
    return answer