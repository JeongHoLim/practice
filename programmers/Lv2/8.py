# https://programmers.co.kr/learn/courses/30/lessons/67257?language=python3

import re
import itertools
def solution(expression):
    answer = 0
    p1 = re.compile('\d+')
    p2 = re.compile("[-*+]")
    nums = list(map(int,p1.findall(expression)))
    ops = p2.findall(expression)
    
    def cal(op,n1,n2):
        if op == "-": return n1-n2
        elif op == "+" : return n1 + n2
        else : return n1*n2    
    
    pd = {}
    per = list(itertools.permutations([str(i) for i in range(3)]))
    for pd['+'],pd['-'],pd['*'] in per:
        print(f"+:{pd['+']}, - : {pd['-']}, * : {pd['*']}")
        n_stack = [nums[0],nums[1]]
        op_stack = [ops[0]]
        equation = f"({nums[0]} {ops[0]} {nums[1]}"
        
        for index in range(1,len(nums)-1):
        
            op1 = op_stack[-1]
            op2 = ops[index]
            n3 = nums[index+1]
            
            print(equation)
            if pd[op1] > pd[op2]:
                temp = eval(equation+")")
                equation = f"({temp}"
            
            op_stack.append(op2)
            equation += f"{op2} {n3}"
        
        
        
        answer = max(answer,abs(eval(equation+")")))    
    

    return answer