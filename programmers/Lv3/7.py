# https://programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    
    for i,row in enumerate(triangle):
        if i == 0: continue
        for j,v in enumerate(row):
            if j == len(row)-1:
                triangle[i][j] += triangle[i-1][j-1]
            elif j == 0:
                triangle[i][j] += triangle[i-1][j]
            else:
                triangle[i][j] += max(triangle[i-1][j],triangle[i-1][j-1])        
    
    return max(triangle[-1])