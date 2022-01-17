
# https://programmers.co.kr/learn/courses/30/lessons/12899?language=python3#

def solution(n):
    answer = ''
    my_dict = ['4','1','2']
    
    r = n
    while r>0:
        r,q = divmod(r,3)
        answer += my_dict[q]
        if q== 0:
            r -= 1
    
    return answer[::-1]