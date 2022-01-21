# https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3#

from itertools import combinations,permutations
import math
def solution(numbers):
    answer = 0
    def is_prime(x):
        if x <= 1: return False
        for i in range(2,int(math.sqrt(x))+1):
            if x % i ==0:
                return False
        
        return True
    
    found = set()
    for i in range(1,len(numbers)+1):
        combi = list(combinations(numbers,i))
        for c in combi:
            for p in permutations(c):
                value = int("".join(p))
                if value not in found and is_prime(value): 
                    answer += 1            
                    found.add(value)
    
    return answer