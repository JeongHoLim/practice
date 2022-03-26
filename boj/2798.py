from itertools import combinations

n,m = list(map(int,input().split()))

num = list(map(int,input().split()))

ans = 0 
for x in combinations(num,3):
    t = sum(x)
    if t > m: continue
    ans = ans if m - t > m - ans else t

print(ans)