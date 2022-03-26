
N = int(input())
stone = list(map(int,input().split()))
number = 0

stone.sort()

for s in stone:
    if s <= number + 1:
        number += s
    else: break

print(number+1)   