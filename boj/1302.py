from collections import defaultdict
n = int(input())

board = defaultdict(int)
for _ in range(n):
    book = input()
    board[book] += 1

trans = [x for x in board.items()]
trans.sort(key=lambda x : (-x[1],x[0]))

print(trans[0][0])