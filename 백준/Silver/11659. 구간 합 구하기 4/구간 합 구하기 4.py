import sys 

input = sys.stdin.readline

n, m = map(int,input().strip().split())

ls = list(map(int,input().split()))

ls.insert(0,0)
for i in range(len(ls)-1):
    ls[i+1] += ls[i]

for _ in range(m):
    
    i,j = list(map(int,input().split()))
    result = ls[j]-ls[i-1]

    print(result)
