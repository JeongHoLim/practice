from collections import defaultdict
def solution(n, k, cmd):
    
    link = defaultdict(list)
    deleted = []    
    for i in range(-1,n+1):
        link[i].extend([i-1,i+1])
    
    cur = k
    for c in cmd:
        op = c.split()
        
        if op[0] == 'C':
            deleted.append([cur,link[cur]])
            l,r = link[cur]
            
            link[l][1],link[r][0] = r,l
            cur = r
            if cur == n:
                cur = l
            
        elif op[0] == 'Z':
            recovered = deleted.pop()
            l,r = recovered[1]
            link[l][1] = link[r][0] = recovered[0]
        else:
            X = int(op[1])
            if op[0] == 'U':
                for _ in range(X):
                    cur = link[cur][0]
            else:
                for _ in range(X):
                    cur = link[cur][1]
    
    answer = ""
    
    for i in range(n):
        l = link[i][0]
        if link[l][1] != i:
            answer += "X"
        else: answer += "O"
            
    return answer