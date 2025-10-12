import sys 

input = sys.stdin.readline

n = int(input())
w_ls = [int(input()) for _ in range(n)]
w_ls.sort() 

answer = 0
for i in range(n):
# i번째(0-index)까지 포함해 총 k = N - i개를 
# 가능 중량 = w[i] * (N - i).
    answer = max(answer, w_ls[i] * (n - i))
print(answer)