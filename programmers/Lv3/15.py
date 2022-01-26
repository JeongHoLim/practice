# https://programmers.co.kr/learn/courses/30/lessons/12946?language=python3

def solution(n):
    answer = []
    
    def hanoi(f,m,t,n,answer):
        if n == 0:
            return
        hanoi(f,t,m,n-1,answer)
        answer.append([f,t])
        hanoi(m,f,t,n-1,answer)
    
    hanoi(1,2,3,n,answer)
    
    return answer