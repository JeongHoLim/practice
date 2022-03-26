n = int(input())

number = 1
ans = 0
while n > 0:
    if number > n:
        number = 1
    n -= number
    number += 1
    ans += 1

print(ans)