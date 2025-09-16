from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

queue = deque()

for i in range(n):
    todo = list(input().split())
    
    do = todo[0] 
    
    if len(todo)>1:
        queue.appendleft(int(todo[1]))
        
    else: 
        if do == "front":
            if len(queue) >0:
                print(queue[-1])
            else: 
                print(-1)
        elif do == "back":
            if len(queue)>0:
                print(queue[0])  
            else:
                print(-1)
        elif do == "size":
            print(len(queue))
        elif do == "empty":    
            if len(queue):
                print(0)
            else:
                print(1)
        elif do == "pop":   
            if len(queue) > 0:
                poped = queue.pop()
                print(poped)
            else: 
                print(-1)