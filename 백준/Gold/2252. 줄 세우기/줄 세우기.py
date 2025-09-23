import sys 
import pprint
from collections import deque
input = sys.stdin.readline
#간선 확인해서 indegree 테이블 채우기 

# indegree 가 0인 정점들을 모두 큐에 넣는다 

# 큐에서 정점을 꺼내어 위상정렬 결과에 추가 

N,M =  map(int,input().split())
# 3 , 2 

graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for i in range(M):
    a,b = map(int,input().split())
    
    graph[a].append(b)
    indegree[b] +=1 

q= deque()
for idx in range(1,len(indegree)):
   if indegree[idx] == 0:
    q.append(idx)

while q:
    current = q.popleft()
    print(current,end=' ')
    for next in graph[current]:
        indegree[next]-=1
        if indegree[next] == 0:
            q.append(next)