
def check(N,candy):
    for i in range(N):
        if candy[i] % 2 :
            candy[i] += 1
    return len(set(candy)) == 1

def teacher(candy,N):
    temp = [0 for _ in range(N)]

    for i in range(N):
        candy[i] //= 2
        temp[(i+1)%N] += candy[i]

    for i in range(N):
        temp[i] += candy[i]
    return temp


def process():
    N,candy = int(input()), list(map(int,input().split()))
    cnt = 0 

    while not check(N,candy):
        cnt += 1
        candy = teacher(candy,N)
    print(cnt)

for i in range(int(input())):
    process()
    