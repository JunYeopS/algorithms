import sys 
from collections import deque 
input = sys.stdin.readline

n = int(input())

stack = deque()

for i in range(n):
    order = list(map(int,input().strip().split()))
    if len(order) >1 :
        stack.append(order[1])
    else: 
        if order[0] == 2:
            if len(stack) > 0:
                poped = stack.pop()
                print(poped)
            else: 
                print(-1)
        elif order[0] == 3:
            print(len(stack))
        elif order[0] == 4:
            if len(stack) == 0: print(1) 
            else: print(0)
        elif order[0] == 5:
            if len(stack) ==0:
                print(-1)
            else:
                print(stack[-1])