N = int(input())
num = []
for _ in range(N):
    num.append(int(input()))

for x in sorted(num):
    print(x)