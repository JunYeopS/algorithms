import sys 
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

graph = [ [] for _ in range(N+1)]

for i in range(1,N):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# 2번 너드부터 순서대로 
visited = [False] * (N+1)
parent = [0]*(N+1)

def dfs(idx ): 
    global dfs
    visited[idx] = True
    for neighbor in graph[idx]:
        if len(graph[idx]) < 1:
            graph[idx].append(1)
        if not visited[neighbor] and graph:
            parent[neighbor] = idx
            dfs(neighbor)

dfs(1)

for ix in range(2,len(parent)):
    print (parent[ix])