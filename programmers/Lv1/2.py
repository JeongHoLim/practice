# https://programmers.co.kr/learn/courses/30/lessons/77484?language=python3

def solution(lottos, win_nums):
    answer = []
    
    check = [0]*46

    
    for l in lottos:
        check[l] = 1
    
    match_count = 0
    for w in win_nums:
        if check[w] == 1: match_count += 1  
    
    zero_num = lottos.count(0)
    min_rank = min(6,7-match_count)
    
    max_rank = max(1,min(7-match_count-zero_num,6))
    
    answer = [max_rank,min_rank]
    
    
    
    return answer