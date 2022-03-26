n = int(input())
seq = []

stack = []
i = 1
ans = ""

for num in range(n):
    data = int(input())
    while data >= i:
        stack.append(i)
        ans += "+"
        i += 1

    if stack and stack[-1] ==  data:
        ans += "-"
        stack.pop()
    else:
        print("NO")
        exit(0)

print("\n".join(ans))

