import sys 
input= sys.stdin.readline
N, M, V = map(int,input().split())

def dfs(idx):
    global visited
    visited[idx] = True
    print(idx, end=' ')
    for next in range(1, N+1):
        if not visited[next] and graph[idx][next]: #방문한적이 없고 현재 인덱스에서 갈수 있는 곳이라면 즉, 간선이 연결 되어 있다면 
            dfs(next)
            
def bfs(V):
    global q, visited 
    if len(q)< 1:
        q.append(V)
        visited[V] = True
    while q: 
        current = q.pop(0)
        print(current,end=' ')
        for next in range(1,N+1):
            if not visited[next] and graph[current][next]:
                visited[next] = True
                q.append(next)


graph = [[False]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)

for i in range(M):
    a,b = map(int,input().split())
    graph[a][b] = True
    graph[b][a] = True

dfs(V)
print("")
visited = [False]*(N+1)
q =[]

bfs(V)