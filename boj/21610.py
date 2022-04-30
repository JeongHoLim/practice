N,M = map(int,input().split())
A = [[] for _ in range(N)]

for i in range(N):
    A[i].extend(map(int,input().split()))

moves = []
for _ in range(M):
    moves.append(list(map(int,input().split())))


cloud = [[N-2,0],[N-2,1],[N-1,0],[N-1,1]]

def move_cloud(cloud,direction,s,n):
    moved = []
    dx,dy = direction[0]*s,direction[1]*s
    for c in cloud:
        moved.append([(c[0]+dx +n)%n,(c[1]+dy+n)%n])

    return moved

def make_rain(cloud,a):
    for c in cloud:
        a[c[0]][c[1]] += 1

def duplicate_water(cloud,a,d,n):

    score =[]
    for c in cloud:
        count = 0
        for i in [2,4,6,8]:
            nx,ny = c[0] + d[i][0],c[1] + d[i][1]
            if 0 > nx or 0 > ny or ny >= n or nx >= n: continue
            if a[nx][ny] > 0 : count += 1
        score.append(count)

    for i in range(len(cloud)):
        x,y = cloud[i]
        a[x][y] += score[i]
        
def make_cloud(cloud,a,n):
    black_list = [[True for _ in range(n)] for _ in range(n)]
    new_cloud = []
    for c in cloud:
        black_list[c[0]][c[1]] = False

    for i in range(n):
        for j in range(n):
            if a[i][j] >= 2 and black_list[i][j]:
                a[i][j] -= 2
                new_cloud.append([i,j])

    return new_cloud


direction = {
    1 : [0,-1],
    2 : [-1,-1],
    3 : [-1,0],
    4 : [-1,1],
    5 : [0,1],
    6 : [1,1],
    7 : [1,0],
    8 : [1,-1]
}

for i in range(M):
    d,s = moves[i]
    cloud = move_cloud(cloud,direction[d],s,N)
    make_rain(cloud,A)
    duplicate_water(cloud,A,direction,N)
    cloud = make_cloud(cloud,A,N)

ans = 0
for i in range(N):
    ans += sum(A[i])

print(ans)