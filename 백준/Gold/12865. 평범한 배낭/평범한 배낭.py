import sys
import pprint as p
input = sys.stdin.readline

N, K = map(int,input().split())

weight, value = [],[]

for i in range(N):
    x,y = list(map(int,input().split()))
    weight.append(x)
    value.append(y)
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1): #
    for j in range(1,K+1):
        if weight[i-1]>j:
            #무게 초과 나면 전에꺼 그냥 가져오고 
            dp[i][j] = dp[i-1][j]
        else:
            #초과 안나면 value더해야지
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-weight[i-1]] + value[i-1])
p.pp(dp[-1][-1])        