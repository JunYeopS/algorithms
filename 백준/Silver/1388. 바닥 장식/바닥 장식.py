import sys 
import pprint as pp
input = sys.stdin.readline

N,M = map(int,input().split())

graph = []

for i in range(N):
    line = list(input().strip())
    graph.append(line)


def dfs (row,col):
    cur = graph[row][col]
    graph[row][col] = 0
    
    if cur == '-':
        # 좌우 확인 
        for i in [-1,1]:
            next = col + i
            # 행 범위 확인 and 다음꺼 check
            if 0<next and next <M and graph[row][next] =="-":
                dfs(row,next)

    elif cur == '|':
        # 상하
        for idx in (-1, 1):
            next = row + idx
            if 0 < next and next < N and graph[next][col] == '|':
                dfs(next, col)

count = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == '-' or graph[i][j] == '|':       
            count += 1   
            dfs(i, j)      
print(count)