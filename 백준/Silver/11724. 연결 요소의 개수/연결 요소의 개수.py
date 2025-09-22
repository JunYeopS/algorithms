import sys 
sys.setrecursionlimit(10**6)
input= sys.stdin.readline


N,M = map(int,input().split())

graph = {i: [] for i in range(1, N+1)}

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


visited= set()

count = 0 
def dfs(graph, start):
    global visited
    if start not in visited:
        visited.add(start)
        for neighbor in graph[start]:
            dfs(graph, neighbor)
            
for i in range(1,N+1):
    if not i in visited:
        dfs(graph,i)
        count +=1

print(count)