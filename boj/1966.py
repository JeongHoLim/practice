from collections import deque
import heapq
T = int(input())

for _ in range(T):
    heap = []
    printList = deque()
    N,M = list(map(int,input().split()))
    temp = list(map(int,input().split()))
    
    for i,v in enumerate(temp):
        printList.append([i,v])
    
    for t in temp:
        heapq.heappush(heap,-t)

    count = 1
    while heap:
        if printList[0][1] < -heap[0]:
            printList.rotate(-1)
        else:
            if printList[0][0] == M:
                print(count)
                break
            heapq.heappop(heap)
            printList.popleft()
            count += 1

