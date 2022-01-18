# https://programmers.co.kr/learn/courses/30/lessons/60058?language=python3

def solution(p):
    answer = ''

    def is_balanced(p):
        return p.count("(") == p.count(")")
    
    def is_correct(p):
        count = 0
        if is_balanced(p):
            for x in p:
                if x =='(': count += 1
                else: count -=1
                
                if count <0: return False
            return True
        return False
    
    def remove_and_transform(p):
        ret = ""
        for c in p[1:-1]:
            if c==')': ret += "("
            else: ret += ")"
                
        return ret
    def func(p):
        if len(p) ==0: return ""
        
        for i in range(2,len(p)+2,2):
            if is_balanced(p[:i]) and is_balanced(p[i:]):
                u,v = p[:i],p[i:]
                if is_correct(u):
                    u += func(v)
                    return u
                else:
                    nc = "(" + func(v) + ")"
                    return nc + remove_and_transform(u)
    answer = func(p)
    
    return answer