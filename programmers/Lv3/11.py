# https://programmers.co.kr/learn/courses/30/lessons/43238?language=python3#

def solution(n, times):
    
    s,e = 0,max(times)*n
    
    while s<=e:
        m = s + (e-s) // 2
        cnt = 0
        for t in times:
            cnt += m//t
        if cnt >= n:
            e = m-1
            answer = m
        else:
            s = m+1
    
    return answer