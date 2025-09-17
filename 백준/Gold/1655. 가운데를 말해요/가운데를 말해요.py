import sys

import heapq

input = sys.stdin.readline
n = int(input())

max_hq=[]
min_hq=[]
for i in range(n):
    node = int(input())

    if len(max_hq)==0:
        heapq.heappush(max_hq,-node)
    else: 
        if node <= -(max_hq[0]):
            heapq.heappush(max_hq,-node)
        else:    
            heapq.heappush(min_hq,node)
    if len(max_hq)- len(min_hq) > 1:
        x = heapq.heappop(max_hq)
        heapq.heappush(min_hq,-x)
    elif len(min_hq) > len(max_hq):
        y = heapq.heappop(min_hq)
        heapq.heappush(max_hq,-y)
    print(-(max_hq[0]))