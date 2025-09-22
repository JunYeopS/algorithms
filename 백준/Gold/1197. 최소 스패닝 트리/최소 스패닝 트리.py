import sys 

input= sys.stdin.readline
sys.setrecursionlimit(10**6)

V, E = map(int,input().split())

edges =[]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # 경로 압축
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[y_root] = x_root
        
for _ in range(E):
    a, b, cost = map(int, input().split())
    edges.append(( cost,a, b))

edges.sort()

parent = [i for i in range(V+1)]
result = 0

for cost, a, b in edges:
    if find(a) != find(b):  # 사이클 확인
        union(a,b)
        result +=cost
        
print(result)