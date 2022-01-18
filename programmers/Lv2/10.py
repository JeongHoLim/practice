# https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3
import collections
import heapq
def solution(numbers):
    
    answer = ''
    
    nums = list(map(str,numbers))
    
    max_len = max(len(x) for x in nums)
    
    original_nums = nums[:]
    for i,v in enumerate(nums):
        while len(nums[i]) < 12:
            nums[i] += v
    
    my_dict = collections.defaultdict(list)
    
    for k,v in zip(nums,original_nums):
        heapq.heappush(my_dict[k],(v,-len(v)))
    
    nums = sorted(nums,reverse=True)
    
    for n in nums:
        answer += my_dict[n].pop(0)[0]
        
    if answer[0] =="0":
        answer="0"
        
    return answer