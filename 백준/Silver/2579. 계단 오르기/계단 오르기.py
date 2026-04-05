import sys 

input = sys.stdin.readline

n = int(input())

ls =[]
for i in range(n):
    ls.append(int(input()))

dp = [0 for _ in range(n)]

dp[0] = ls[0]

if n == 1:
    print(dp[0])
elif n == 2:
    dp[1] = ls[0] + ls[1]
    print(dp[1])
else:
    dp[1] = ls[0] + ls[1]
    dp[2] = max(ls[0],ls[1]) + ls[2]
        
    for i in range(3,n):
        dp[i] = max(dp[i-2] + ls[i], dp[i-3] +ls[i-1]+ ls[i] )

    print(dp[n-1])
