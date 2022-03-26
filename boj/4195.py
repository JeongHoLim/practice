# 11:20

import sys
sys.setrecursionlimit(10**6)

def union(x,y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        net_size[x] += net_size[y]


def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]


n = int(input())

for _ in range(n):
    f = int(input())
    
    parent = dict()
    net_size = dict()

    for _ in range(f):
        f1,f2 = input().split() 

        if f1 not in parent:
            parent[f1] = f1
            net_size[f1] = 1

        if f2 not in parent:
            parent[f2] = f2
            net_size[f2] = 1

        union(f1,f2)

        print(net_size[find(f1)])

