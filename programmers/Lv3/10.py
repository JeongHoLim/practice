# https://programmers.co.kr/learn/courses/30/lessons/42898?language=python3#

def solution(m, n, puddles):
    
    dp = [[0 for _ in range(m+1)]for _ in range(n+1)]
    path = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for y,x in puddles:
        dp[x][y] = float('inf')
    for i in range(m+1):
        dp[0][i] = float('inf')
    for i in range(n+1):
        dp[i][0] = float('inf')
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i ==1 and j == 1: 
                dp[i][j],path[i][j] =0,1
                continue
            elif dp[i][j] > 0: continue
            
            c1,c2 = dp[i-1][j]+1,dp[i][j-1]+1
            
            dp[i][j] = min(c1,c2)
            if c1 == c2:
                path[i][j] = path[i-1][j] + path[i][j-1]
            else:
                path[i][j] = path[i-1][j] if dp[i][j] == c1 else path[i][j-1]
    
    return path[n][m] % 1000000007