import sys

input = sys.stdin.readline

max = 0
pos = (1,1)

for i in range(9):
    ls = list(map(int,input().split()))
    for j in range(9):
        
        if ls[j] > max: 
            max = ls[j]
            pos = (i+1, j+1)

print(max)
print(*(pos))