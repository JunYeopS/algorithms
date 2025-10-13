import sys 

input = sys.stdin.readline

n = int(input())

def comb(n, m):
    result = 1
    for i in range(n):
        result *= (m - i)
        result //= (i + 1)
    return result

for _ in range(n):
    n,m = map(int, input().split())
    print(comb(n,m))