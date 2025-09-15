import sys

input= sys.stdin.readline

n = input()
ls = list(map(int,input().split()))

""" 기록용"""
result = [] 
s = [] #stack

for i in range(len(ls)): # 4 -3- 2 -1 -0
    
    while s and ls[s[-1]] <= ls[i]:        
        s.pop()
    if not s:
        result.append(0)
    else:
        result.append(s[-1]+1)
    s.append(i)
print(" ".join(map(str, result)))          