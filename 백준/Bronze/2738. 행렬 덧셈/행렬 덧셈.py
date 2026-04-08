import sys

input = sys.stdin.readline

n, m = map(int,input().split())

a = []
b = []

for i in range(n):
    ls = list(map(int, input().strip().split()))
    a += [ls]

for i in range(n):
    ls = list(map(int, input().strip().split()))
    b += [ls]

for i in range(n):
    for j in range(m):
        b[i][j] += a[i][j]
    print(*b[i])