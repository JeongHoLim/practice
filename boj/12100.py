n = int(input())
board = []

for i in range(n):
    board.append(list(map(int,input().split())))

ans = float('-inf')

def calculate(row):
    save = []
    while row:
        block1 = block2 = None
        while row:
            block1 = row.pop()
            if block1 != 0 : break
            block1 = None

        while row:
            if row[-1] != 0 and row[-1] != block1: break
            block2 = row.pop()
            if block2 != 0 : break
            block2 = None
        
        if block2:
            save.append(block1*2)
        elif block1:
            save.append(block1)
    
    while len(save) < n:
        save.append(0)
    return save[::-1]


def move(board,dir,n):

    new_board = None
    if dir%2== 0:
        # to right
        new_board = [[] for _ in range(n)]
        if dir == 0:
            for i in range(n):
                new_board[i] = calculate(board[i][:])
        else:
            for i in range(n):  
                new_board[i] = calculate(board[i][::-1])

    else:
        temp_board = [[board[i][j] for i in range(n)] for j in range(n)]
        if dir == 1:
            # to down
            for i in range(n):
                temp_board[i] = calculate(temp_board[i][:])
        else: 
            # to up
            for i in range(n):
                temp_board[i] = calculate(temp_board[i][::-1])

        new_board = [[temp_board[i][j] for i in range(n)] for j in range(n)]

    return new_board

def updateAnswer(board,n):
    temp = float('-inf') 
    for i in range(n):
        temp = max(temp,max(board[i]))
    globals()["ans"] = max(temp,globals()["ans"])

def dfs(board,n,count):

    if count >= 5:
        updateAnswer(board,n)
        return
    for i in range(4):
        new_board = move(board,i,n)
        dfs(new_board,n,count+1)

dfs(board,n,0)

print(ans)