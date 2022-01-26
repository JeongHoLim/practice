# https://programmers.co.kr/learn/courses/30/lessons/43164

from collections import defaultdict
def solution(tickets):
    answer = []
    
    graph = defaultdict(list)
    
    for f,t in tickets:
        graph[f].append([t,True])
        
    ticket_num = 0
    for f in graph.keys():
        graph[f].sort()
        ticket_num += len(graph[f])
        
    def dfs(graph,current,history,route,n):
        
        history.append(current)
        if n == 0:
            route.extend(history)
            return True
        
        for i,t in enumerate(graph[current]):
            if not t[1]: continue
                
            graph[current][i][1] = False

            if dfs(graph,t[0],history,route,n-1):
                return True
            
            graph[current][i][1] = True
        
        history.pop()     
        return False
        
        
    dfs(graph,"ICN",[],answer,ticket_num)
    
    return answer