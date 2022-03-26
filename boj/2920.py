from numpy import spacing


num = list(map(int,input().split()))

asc = des = True

for i in range(len(num)-1):
    if num[i] > num[i+1]:
        asc = False
    elif num[i] < num[i+1]:
        des = False

if asc:
    print("ascending")
elif des:
    print("descending")
else:
    print("mixed")