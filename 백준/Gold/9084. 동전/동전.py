import sys 
import pprint as pp
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    coin_count = int(input())
    coin_ls = list((map(int,(input().strip()).split())))
    target = int(input())
    dp = [0] * (target + 1)
    dp[0] = 1
    for coin in coin_ls: 
        for i in range(coin, target+1): 
            dp[i] += dp[i-coin]
    
    pp.pp((dp[-1]))