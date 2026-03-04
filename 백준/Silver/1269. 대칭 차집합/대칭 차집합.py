import sys 

input = sys.stdin.readline

a,b = input().split()

a_list = set(map(int,input().split()))
b_list = set(map(int,input().split()))

count = len(a_list ^ b_list)

print(count)