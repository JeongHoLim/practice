# https://programmers.co.kr/learn/courses/30/lessons/92334?language=python3
import collections

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report_dict = collections.defaultdict(list)

    for rep in report:
        info = rep.split()
    
        if info[0] not in report_dict[info[1]]:
            report_dict[info[1]].append(info[0])
    
    for user_id, report_users in report_dict.items():
        if len(report_users) >= k:
            for u in report_users:
                answer[id_list.index(u)] += 1
            
    
    return answer