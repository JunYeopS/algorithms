import sys 
import pprint as p
input = sys.stdin.readline

n = int(input())

board = [list(map(int,input().strip().split())) for _ in range(n)]

dp= [([0]*n) for _ in range(n)]

dp[0][0] = 1

for i in range(n):
    for j in range(n):

            # 점프 길이 0 곳은 패스 
            mov_num = board[i][j]
            if mov_num == 0:
                continue  

            # 오른쪽 이동
            mov_right = j + mov_num
            if mov_right < n:
                dp[i][mov_right] += dp[i][j]

            # 아래 이동
            mov_down = i + mov_num
            if mov_down < n:
                dp[mov_down][j] += dp[i][j]

print(dp[-1][n-1])