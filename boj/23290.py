from copy import deepcopy

m,s = map(int,input().split())
grid = [[[] for _ in range(4)] for _ in range(4)]
smell = [[0 for _ in range(4)] for _ in range(4)]
directions = {
    0: [0,-1],
    1: [-1,-1],
    2: [-1,0],
    3: [-1,1],
    4: [0,1],
    5: [1,1],
    6: [1,0],
    7: [1,-1]
}


for i in range(m):
    fx,fy,d = map(int,input().split())
    grid[fx-1][fy-1].append(d-1)

s_xy = list(map(lambda x : int(x)-1,input().split()))

def get_valid_move(smell,x,y,d,directions,s_xy):

    od = d
    for _ in range(8):
        dx,dy = directions[d]
        f_xy = [x+dx,y+dy]
        if f_xy[0]<0 or f_xy[0] >= 4 or f_xy[1] <0 or f_xy[1] >=4:
            d = (d+7)%8
        elif s_xy == f_xy:
            d = (d+7)%8
        elif smell[f_xy[0]][f_xy[1]] >0:
            d = (d+7)%8
        else:
            return f_xy[0],f_xy[1],d

    return x,y,od

def move_fish(grid,smell,directions,s_xy):
    
    new_grid = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if len(grid[i][j]) == 0: continue
            for d in grid[i][j]:
                dx,dy,nd = get_valid_move(smell,i,j,d,directions,s_xy)
                new_grid[dx][dy].append(nd)
            
    return new_grid

def is_valid_move(x,y):
    return (0<=x<4) and (0<=y<4)


def compare(c1,c2,paths):
    global path
    t1,t2 = sum(map(lambda x: x[2],c1)),sum(map(lambda x : x[2],c2))
    if t1 > t2:
        return True
    elif t1 == t2:
        return "".join(map(str,path)) > "".join(map(str,paths))
    

# 상은 1, 좌는 2, 하는 3, 우는 4로 변환한다. 
def move_shark(grid,smell,s_xy,path,caught=[],step = 0):

    if step == 3:
        if compare(caught,globals()["caught"],path):
            globals()["caught"] = caught[:]
            globals()["next_move"] = s_xy[:]
            globals()["path"] = path[:]
        return 

    possible_move = [[-1,0],[0,-1],[1,0],[0,1]]
    x,y = s_xy

    for k,dxy in enumerate(possible_move,1):
        temp = []
        dx,dy = dxy
        if not is_valid_move(x+dx,y+dy): continue
        if len(grid[x+dx][y+dy]) > 0:
            temp = grid[x+dx][y+dy][:]
            grid[x+dx][y+dy] = []
            caught.append([x+dx,y+dy,len(temp)])
        
        move_shark(grid,smell,[x+dx,y+dy],path + [k],caught,step+1)

        if temp:
            grid[x+dx][y+dy] = temp[:]
            caught.pop()

    return 

def remove_smell(smell,cnt):
    for i in range(4):
        for j in range(4):
            if cnt-smell[i][j] == 2:
                smell[i][j] = 0

def duplicate_fish(duplicate,grid):
    for i in range(4):
        for j in range(4):
            if len(duplicate[i][j]) > 0 :
                grid[i][j].extend(duplicate[i][j])
    

def remove_fish(grid,smell,caught,index):
    for c in caught:
        grid[c[0]][c[1]] = []
        smell[c[0]][c[1]] = index

next_move = []
for i in range(s):
    duplicate = deepcopy(grid)
    caught,path = [],[5,5,5]
    grid = move_fish(grid,smell,directions,s_xy)
    move_shark(grid,smell,s_xy,[])
    s_xy = next_move[:]
    remove_fish(grid,smell,caught,i+1)
    duplicate_fish(duplicate,grid)
    remove_smell(smell,i+1)    


k = 0
for i in range(4):
    for j in range(4):
        k += len(grid[i][j])

print(k)