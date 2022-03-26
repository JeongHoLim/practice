
def reverse(matrix,x,y):
    for i in range(x,x+3):
        for j in range(y,y+3):
            matrix[i][j] = "0" if matrix[i][j] == "1" else "1" 

def check(a,b,n,m):
    for i in range(n):
        if a[i] != b[i]:
            return False
    return True

def change(a,b,n,m):
    count = 0 
    if check(a,b,n,m):
        return count

    for i in range(n-2):
        for j in range(m-2):
            if a[i][j] != b[i][j] :
                count += 1
                reverse(a,i,j)
                if check(a,b,n,m):
                    return count
    
    return -1

n,m = list(map(int,input().split()))
a = [list(list(input())) for _ in range(n)]

b = [list(list(input())) for _ in range(n)]
    

print(change(a,b,n,m))