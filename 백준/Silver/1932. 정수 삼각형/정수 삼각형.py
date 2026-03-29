import sys 
from pprint import pprint

input = sys.stdin.readline

n = int(input())

ls =[]
for i in range(n):
    
    ls.append(list(map(int,input().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]

dp[n-1] = ls[n-1]

for i in range(n-2,-1,-1):
    for j in range(i+1):
        
        dp[i][j] = max(dp[i+1][j], dp[i+1][j+1]) + ls[i][j]
            
print(dp[0][0])
