import sys 

input =sys.stdin.readline

N= int(input())
V = int(input())

graph = [[] for i in range(N+1)]

for _ in range(V):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향 연결

visited = [False]*(N+1);
count = -1

def dfs(idx):
    global visited,count
    
    if not visited[idx]:
        visited[idx] = True
        for neighbor in graph[idx]:
            dfs(neighbor)
        count +=1

dfs(1)
print(count)