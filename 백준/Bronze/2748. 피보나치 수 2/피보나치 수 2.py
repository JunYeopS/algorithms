import sys 
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(n+1)]

def fib(num):
    global dp
    dp[1] = 1
    for i in range(2,n+1,1):
        dp[i] = dp[i-1] + dp[i-2]
    return 

fib(n)
print(dp[-1])