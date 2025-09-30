import sys 
import pprint as p
import math
input = sys.stdin.readline

positive = math.inf
N = int(input())
matrix = [tuple(map(int, input().split())) for i in range(N)]

dp = [[positive]*(N) for _ in range (N)]

for _ in range(N):
    dp[_][_] = 0

for length in range(2,N+1):
    for i in range(N-length+1):
        j = i + length - 1
        for k in range(i,j):
            total = matrix[i][0] * matrix[j][1] *  matrix[k][1]
            dp[i][j] = min(dp[i][j],dp[i][k]+dp[k+1][j]+total)
p.pp(dp[0][-1])