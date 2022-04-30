from collections import deque
N,M,k = map(int,input().split())

my_map = [[] for _ in range(N)]

for i in range(N):
    my_map[i].extend(map(int,input().split()))

w,u,e,d = 4,1,3,6
n,s = 2,5

def roll_dice(w,u,e,d,n,s,direction):
    if direction == 1: # 동
        return d,w,u,e,n,s
    elif direction == 3: # 서
        return u,e,d,w,n,s
    elif direction == 0: # 남
        return w,n,e,s,d,u
    else: # 북
        return w,s,e,n,u,d

def get_score(my_map,dxy,x,y,n,m):
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue = deque([[x,y]])
    count = 0 # 현 위치 포함
    level = my_map[x][y]
    visited[x][y] = True

    while queue:
        cur_node = queue.popleft()
        count += 1
        for dx,dy in dxy:
            nx,ny = cur_node[0] + dx,cur_node[1]+dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if my_map[nx][ny] == level and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx,ny])
        
    return count*level

def check_direction(d,dxy,x,y,n,m):
    nx,ny = x + dxy[d][0],y+dxy[d][1]
    if (0<=nx < n) and (0<=ny<m):
        return d
    return (d+2)%4

def choose_direction(A,B,d):
    if A == B : return d
    elif A < B : return (d+1)%4
    else: return (d+3)%4

direction,score = 1,0
x,y = 0,0
dxy = [[1,0],[0,1],[-1,0],[0,-1]]

for _ in range(k):
    direction = check_direction(direction,dxy,x,y,N,M)
    w,u,e,d,n,s = roll_dice(w,u,e,d,n,s,direction)
    x,y = x + dxy[direction][0], y+dxy[direction][1]
    score += get_score(my_map,dxy,x,y,N,M)    
    direction = choose_direction(d,my_map[x][y],direction)

print(score)
