
# https://programmers.co.kr/learn/courses/30/lessons/12973?language=python3

def solution(s):
    
    check,stack = {},[]
    alpha = "abcdefghijklmnopqrstuvwxyz"
    reversed_s = s[::-1]
    for a in alpha:
        check[a] = len(s) - reversed_s.find(a) + 1

    i = 0
    while True:
        if i == len(s):
            if stack: answer = 0
            else: answer = 1
            break
            
        cur = s[i]
        if check[cur] < i or len(stack) > len(s)-i:
            answer = 0
            break
        
        if stack and stack[-1] == cur:
            stack.pop()
        else:
            stack.append(cur)
        i += 1
    
    return answer