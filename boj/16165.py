from collections import defaultdict
n,m = list(map(int,input().split()))
gGroup = defaultdict(list)
gPeople = defaultdict(str)
for _ in range(n):
    gName = input()
    gNum = int(input())
    for _ in range(gNum):
        name = input()
        gGroup[gName].append(name)
        gPeople[name] = gName

for _ in range(m):
    name = input()
    quiz = input()
    if quiz == "1":
        print(gPeople[name])
    else:
        print("\n".join(sorted(gGroup[name])))