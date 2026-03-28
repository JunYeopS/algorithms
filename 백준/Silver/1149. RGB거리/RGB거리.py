import sys

input = sys.stdin.readline
n = int(input())

dp = [[0 for i in range(3)] for _ in range(n)]
ls = []
for _ in range(n):
    red, green, blue = map(int,input().split())
    ls.append([red,green,blue])

dp[0] = ls[0]

for i in range(1,n):
    for j in range(3):  
        prev_min = min(dp[i-1][:j]+dp[i-1][j+1:])
        
        dp[i][j] = prev_min + ls[i][j]

print(min(dp[n-1]))
