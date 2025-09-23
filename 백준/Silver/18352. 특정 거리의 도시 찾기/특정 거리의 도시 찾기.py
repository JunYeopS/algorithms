import sys 
from collections import deque
input = sys.stdin.readline

N, M , K ,X = map(int,input().split())

graph = [ [] for _ in range(N+1)]

for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    
# print(graph) #[[], [2, 3], [3, 4], [], []] 

visited = [False] * (N+1)
q = deque()
result = []

def bfs(idx): 
    global visited
    is_K = False
    q.append(idx)
    visited[idx[0]] = True
    
    while q:
        current, count = q.popleft()

        if count == K:
            is_K = True
            result.append(current)
            continue
        for next in graph[current]:
            if not visited[next] :
                visited[next] = True
                q.append([next,count+1])
                
    if is_K ==False:
        print(-1) 
    else:
        print("\n".join(map(str,sorted(result))))      

bfs([X,0])
