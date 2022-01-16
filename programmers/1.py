
# https://programmers.co.kr/learn/courses/30/lessons/67257?language=python3#

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
    
    priority_dict = {}
    per = list(itertools.permutations([str(i) for i in range(3)]))
    for i,j,k in per:
        
        priority_dict['+'] = i
        priority_dict['-'] = j
        priority_dict['*'] = k
        
        n_stack = [nums[0],nums[1]]
        op_stack = [ops[0]]
    
        for index in range(1,len(nums)-1):
        
            op1 = op_stack[-1]
            op2 = ops[index]
            n3 = nums[index+1]

            while priority_dict[op1] >= priority_dict[op2]:
                n2 = n_stack.pop()
                n1 = n_stack.pop()
                temp = cal(op_stack.pop(),n1,n2)
                n_stack.append(temp)
            
                if len(op_stack) == 0: break
                op1 = op_stack[-1]
                
            op_stack.append(op2)
            n_stack.append(n3)
        
        if op_stack:
            n2 = n_stack.pop()
            while op_stack: 
                op = op_stack.pop()
                n1 = n_stack.pop() 
                n2 = cal(op,n1,n2)
                    
        answer = max(answer,abs(n2))    
    

    return answer

print(type(eval("1+2")))