import sys

input = sys.stdin.readline

n = int(input())

board = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(n): 
    paper = tuple(map(int,input().strip().split()))
    
    for i in range(paper[0], paper[0]+10, 1): 
        for j in range(paper[1], paper[1]+10, 1):
                board[i][j] = 1

count = 0

for i in range(100):
    for j in range(100):
        if board[i][j] == 1: 
            count +=1
            
print(count)