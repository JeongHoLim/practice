class List(list): pass

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        answer = []
        def makeAnswer(idx,path,temp_sum):
            if idx == n: return

            if temp_sum == target:
                answer.append(path[:])
                return

            for i in range(idx,n):
                check = temp_sum + candidates[i]
                if check > target:
                    return
                path.append(candidates[i])
                makeAnswer(i,path,check)
                path.pop()
        
        candidates.sort()
        makeAnswer(0,[],0)
        return answer

s = Solution()

candidates = [2,3,6,7]
target = 7

print(s.combinationSum(candidates,target))