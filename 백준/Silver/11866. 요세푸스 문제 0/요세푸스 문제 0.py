from collections import deque

n,k = map(int,input().split())

queue = deque()

sequence = []

for i in range(1,n+1,1):
    queue.append(i)

while len(queue)>0:
    
    queue.rotate(-k+1)
    poped = queue.popleft()
    sequence.append(poped)

print(f"<{', '.join(map(str, sequence))}>")