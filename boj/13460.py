from collections import deque

n,m = map(int,input().split())
board = [[] for _ in range(n)]


blue,red = [],[]
for i in range(n):
    board[i].extend(*input().split())
    if 'B' in board[i]:
        blue.append([i,board[i].index('B')])
        board[i][blue[0][1]] = "."
    if 'R' in board[i]:
        red.append([i,board[i].index('R')])
        board[i][red[0][1]] = "."

ans = 11


def roll(board,coord,dir,n,m):

    x,y = coord[0],coord[1]
    flg = False
    while True:
        x,y = x + dir[0], y + dir[1]
        if not ((0 <= x <= n) and (0 <= y <= m)): break
        if board[x][y] == "O": 
            flg = True
            break
        if board[x][y] != '.': break
        
    return [x-dir[0],y-dir[1]],flg
    

def nextMove(board,cur,dir,n,m):

    blue,red = cur[1],cur[2]    
    first = None
    if dir == [0,1]:
        first = "r" if red[1] > blue[1] else "b"
    elif dir == [1,0]:
        first  = "r" if red[0] > blue[0] else "b"
    elif dir == [0,-1]:
        first = "r" if red[1] < blue[1] else "b"
    else:
        first = "r" if red[0] < blue[0] else "b"


    if first == "r":
        res1,flg1 = roll(board,red,dir,n,m)
        if not flg1: 
            board[res1[0]][res1[1]] = 'R'
        res2,flg2 = roll(board,blue,dir,n,m)
        board[res1[0]][res1[1]] = '.'

        if flg2:
            return False
        elif flg1 : return [-1]

    else:
        res1,flg1 = roll(board,blue,dir,n,m)
        if flg1: return False

        board[res1[0]][res1[1]] = 'B'
        res2,flg2 = roll(board,red,dir,n,m)
        board[res1[0]][res1[1]] = '.'
        
        if flg2: return [-1]

    if first == "r" :
        return res2,res1
    else:
        return res1,res2


def bfs(board,blue,red,n,m):

    queue = deque([[6,*blue,*red,0]])
    directions = [[0,1],[1,0],[0,-1],[-1,0]]

    while queue:
        cur = queue.popleft()
        if cur[3] > 10: continue

        for i,v in enumerate(directions):
            if abs(cur[0]-i) == 2: continue  

            next_move = nextMove(board,cur,v,n,m)

            if next_move:
                if next_move == [-1]:
                    ans = globals()["ans"]
                    globals()["ans"] = min(ans,cur[3]+1)
                    break
                else:
                    if cur[1] != next_move[0] or cur[2] != next_move[1]:
                        queue.append([i,*next_move,cur[3]+1])



bfs(board,blue,red,n,m)

ans = -1 if ans == 11 else ans
print(ans)