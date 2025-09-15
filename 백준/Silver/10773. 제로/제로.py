import sys

input = sys.stdin.readline

n = int(input())

ls = []
for i in range(n):
    num = int(input())
    
    if num >0: 
        ls.append(num)
    else:
        ls.pop()
    
print(sum(ls))