class List(list): pass

from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        phone = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        return list(map("".join,product(*(phone[x] for x in digit))))




s = Solution()
digit = "23"
print(s.letterCombinations(digit))