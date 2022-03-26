n = int(input())

num = []
for _ in range(n):
    num.append(list(map(int,input().split())))

for x,y in sorted(num):
    print(x,y)
