#  7시 54분
from collections import deque
T = int(input())

for _ in range(T):
    tc = input()
    cursor = 0
    L = []
    R = deque()

    for command in tc:
        if command == "<":
            if L:
                R.appendleft(L.pop())
        elif command == ">":
            if R:
                L.append(R.popleft())
        elif command == "-":
            if L:
                L.pop()
        else:
            L.append(command)
    password = "".join(L) + "".join(R)
    print(password)