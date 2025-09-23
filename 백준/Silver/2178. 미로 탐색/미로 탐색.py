import sys 
import pprint

input = sys.stdin.readline

N,M = map(int, input().split())

graph = []

for i in range(N):
    row = list(map(int,input().strip()))
    graph.append(row)

q=[]

dx = [-1, 1, 0, 0]   # 상, 하, 좌, 우
dy = [0, 0, -1, 1]

def bfs(x , y):
    global q
    if len(q)<1 :
        q.append((x,y))

    while q : 
        current = q.pop(0)
        x= current[0]
        y= current[1]
        for i in range(4):
            if  0<= x+dx[i] <N and 0 <= y + dy[i] < M:
                nx = x + dx[i]
                ny = y + dy[i]
                if graph[nx][ny]==1:
                    q.append((nx,ny))
                    graph[nx][ny] = graph[x][y]+1

bfs(0,0) 

print(graph[N-1][M-1])