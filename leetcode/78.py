class List(list):pass
from collections import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        answer = [[]]
        for i in range(1,n+1):
            answer.extend(map(list,combinations(nums,i)))
            
        return answer