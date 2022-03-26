import heapq

k,n = list(map(int,input().split()))
prime = list(map(int,input().split()))

heap = []
for p in prime:
    heapq.heappush(heap,p)

count = 0
check = set()
while count < n:
    cur = heapq.heappop(heap)
    if cur in check: continue
    count += 1
    check.add(cur)
      
    for x in prime:
        if cur*x < 2**32:
            heapq.heappush(heap,x*cur)
    

print(cur)
