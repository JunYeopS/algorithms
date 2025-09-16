from collections import deque

queue = deque()

n = int(input())

for i in range(1,n+1,1):
    queue.append(i)
    
for j in range(len(queue)-1):
    
    x= queue.popleft()
    
    queue.rotate(-1)

for ans in queue:
    print(ans)