class List(list): pass

from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(map(list,permutations(nums)))


s = Solution()
nums = [1,2,3]
print(s.permute(nums))