n = int(input())
B = list(map(int,input().split()))

temp = 0
A = []
for i,v in enumerate(B,1):
    cur = v*i-temp
    A.append(cur)
    temp += cur

for x in A:
    print(x,end= " ")

