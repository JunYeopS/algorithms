import heapq
import sys 

n = int(input())

input = (sys.stdin.readline)
ls = [int(input()) for _ in range(n)]

heap = []

for i in ls: 
    if i == 0:
        if len(heap)>0:
            poped = heapq.heappop(heap)
            print(-poped)
        else:
            print(0)
    else:
        heapq.heappush(heap,-i)