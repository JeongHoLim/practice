import sys
from collections import defaultdict
n = int(input())
arr = []
count = defaultdict(int)
for _ in range(n):
    data = int(sys.stdin.readline())
    arr.append(data)
    count[data] += 1

temp = sorted(count.items(),key=lambda x : (-x[1],x[0]))
cAns = temp[1][0] if n > 1 and temp[0][1] == temp[1][1]  else temp[0][0]
print(int(round(sum(arr)/n,0)))
print(sorted(arr)[n//2])
print(cAns)
print(max(arr)-min(arr))