
n = input()

my_set = set()
for item in input().split():
    my_set.add(item)

m = input()

for item in input().split():
    if item in my_set:
        print(1)
    else:
        print(0)