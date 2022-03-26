n = int(input())
cmp = "1"

while n >= eval(cmp):
    cmp += "1"
if len(cmp) == 1:
    print(1)
else: print(len(cmp)-1)