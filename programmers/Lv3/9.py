# https://programmers.co.kr/learn/courses/30/lessons/42895?language=python3

import itertools
def solution(N, number):
    if N == number: return 1
    answer = -1
    dp = [{0},{N}]    
    def add(dp,l,r,idx,N):
        dp[idx].add(l+r)
        dp[idx].add(l-r)
        dp[idx].add(-l+r)
        dp[idx].add(l*r)
        if str(l).count(N) == len(str(l)) and str(r).count(N) == len(str(r)):
            dp[idx].add(eval(f"{l}{r}"))
        if r != 0:
            dp[idx].add(l//r)
        if l != 0:
            dp[idx].add(r//l)
            
        
    for idx in range(2,9):
        dp.append(set())
        i,j = 1,idx-1
        while i <= j:
            pd = list(itertools.product(dp[i],dp[j]))
            for l,r in pd:
                add(dp,l,r,idx,str(N))
            i,j = i+1,j-1
            if number in dp[idx]:
                answer = idx
                break
        if answer != -1:
            break
            
    return answer