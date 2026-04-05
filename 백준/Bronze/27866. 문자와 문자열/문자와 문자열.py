import sys

input = sys.stdin.readline

s = list(input().strip())
target = int(input())

print(s[target-1])