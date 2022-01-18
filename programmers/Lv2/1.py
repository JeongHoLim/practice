
# https://programmers.co.kr/learn/courses/30/lessons/42888?language=python3

import collections
def solution(record):
    answer = []
    
    my_dict = collections.defaultdict(str)
    action_dict =  {"Enter" : "님이 들어왔습니다.","Leave":"님이 나갔습니다."}

    for info in record[::-1]:
        parsed = info.split()
        if len(parsed) == 2: continue
        action,user_id,nick_name = parsed
        
        if my_dict[user_id]=="":
            my_dict[user_id] = nick_name
    
    for info in record:
        parsed = info.split()      
        if parsed[0] == "Change": continue
        
        action,user_id = parsed[0],parsed[1]
        
        answer.append(my_dict[user_id]+action_dict[action])
        
        
    return answer