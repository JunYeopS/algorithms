import sys 

input = sys.stdin.readline

n = int(input())

ls = list(map(int, input().split()))

dp = [0 for _ in range(n)]

dp[0] = ls[0]

for i in range(n-1):
    
    sum = dp[i]+ls[i+1]
    
    if sum < ls[i+1]:
        dp[i+1] = ls[i+1]
    else:
        dp[i+1] = sum


print(max(dp))

