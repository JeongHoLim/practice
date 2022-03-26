import sys
n = int(input())
num = [0 for _ in range(2000001)]
for _ in range(n):
    data = int(sys.stdin.readline())
    num[data+1000000] += 1

for i in range(2000001):
    if num[i] != 0:
        for _ in range(num[i]):
            print(i-1000000)
