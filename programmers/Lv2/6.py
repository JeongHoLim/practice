# https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3

def solution(numbers, target):
    answer = 0
    
    def func(nums,i,n,t,res):
        if i == n:
            if sum(nums) == t:
                res[0] += 1
            return            
        func(nums,i+1,n,t,res)
        nums[i] *= -1
        func(nums,i+1,n,t,res)
        
    res = [0]
    func(numbers[:],0,len(numbers),target,res)
    answer = res[0]
    return answer