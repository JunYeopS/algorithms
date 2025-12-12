import sys

input = sys.stdin.readline

cnt = int(input())
n = input().strip()
ls = list(map(int, n))

total = 0

for i in ls:
    total +=i
    
print(total)