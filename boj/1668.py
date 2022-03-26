n = int(input())

tr = []

for _ in range(n):
    tr.append(int(input()))

front = rear = 1
front_max = tr[0]

for i in range(1,len(tr)):
    if front_max < tr[i]:
        front += 1
        front_max = tr[i]

tr.reverse()
rear_max = tr[0]
for i in range(1,len(tr)):
    if rear_max < tr[i]:
        rear += 1
        rear_max = tr[i]

print(front)
print(rear)