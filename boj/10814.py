n = int(input())
user = []
for i in range(n):
    age,name = input().split()
    user.append([int(age),name,i])

for u in sorted(user,key=lambda x : (x[0],x[2])):
    print(u[0],u[1])
        