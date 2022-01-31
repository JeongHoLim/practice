# 332. Reconstruct Itinerary
from collections import defaultdict

class List(list): pass
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        answer = []
        for f,t in sorted(tickets,reverse=True):
            graph[f].append(t)
        
        def dfs(f):
            while graph[f]:
                dfs(graph[f].pop())
            answer.append(f)
        dfs("JFK")

        return answer[::-1]

s = Solution()

tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
print(s.findItinerary(tickets))