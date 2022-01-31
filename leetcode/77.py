class List(list):pass
from itertools import combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(map(list,combinations([i for i in range(1,n+1)],k)))


s = Solution()
n,k = 4,2
print(s.combine(n,k))