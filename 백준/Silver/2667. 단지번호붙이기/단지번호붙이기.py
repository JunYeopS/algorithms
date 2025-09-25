import sys
import pprint as p
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
graph = [list(map(int, input().strip())) for _ in range(N)]

# p.pp(graph)

# 상하좌우 
dx = [0, 0, -1, 1]
dy = [1, -1, 0 ,0]
count = 0

result= []
q = deque()
def bfs(x, y):
    global count
    graph[x][y] = 0
    q.append([x, y])
    while q:
        current = q.popleft()
        # 료이키 텐카이
        for i in range(4):
            next_x = current[0] + dx[i]
            next_y = current[1] + dy[i]
            if 0 <= next_x < N and 0 <= next_y < N and graph[next_x][next_y] == 1:
                graph[next_x][next_y] = 0
                count += 1
                q.append((next_x, next_y))

for x in range(N):
    for y in range(N):
        if graph[x][y] == 1:
            count = 1
            bfs(x, y)
            result.append(count)
print(len(result))
result.sort()
for i in result:
    print(i)