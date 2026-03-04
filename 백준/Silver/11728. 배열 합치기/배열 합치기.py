import sys 

input = sys.stdin.readline

a,b = map(int,input().split())

a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))

ans = sorted([*a_list,*b_list])

print(*ans)