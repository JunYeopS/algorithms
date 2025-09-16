from collections import deque
import sys
input = sys.stdin.readline

n = int(input().strip())              # 보드 크기 (n x n)

board = [[0]*n for _ in range(n)] # 보드: 0=빈칸, 1=사과, 2=뱀

# 사과 입력 (1-index → 0-index 변환)
apple_num = int(input().strip())
for _ in range(apple_num):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1

# 방향 전환 스케줄 (시간:int, 회전:문자 'L'/'D')
movement_num = int(input().strip())
moves = deque()
for _ in range(movement_num):
    t, d = input().split()            # 예: "3 D"
    moves.append((int(t), d))

snake = deque()
snake.append((0, 0))                  # 0-index 기준 (0,0)에서 시작
board[0][0] = 2                       # snake 시작위치 

t = 0
total_move = 1

# 방향: 오른쪽(시작)
#       우, 하, 좌, 상 (시계방향)
dirs = [(0,1), (1,0), (0,-1), (-1,0)]
dir_idx = 0

while True:
    
    head_row, head_col = snake[-1]
     # 현재 진행 방향(행/열 변화량)
    d_row, d_col = dirs[dir_idx]
    next_row, next_col = head_row + d_row, head_col + d_col
    
    # 충돌이면 종료
    if (not(next_row>=0) and not(next_row < n)) and ((next_col>=0) and (next_col<n)):
        break
    if not (0 <= next_row < n and 0 <= next_col < n):
        break
        
    next_cell = board[next_row][next_col]
    tail_row, tail_col = snake[0]
    
    # 몸 충돌 (단, 다음 칸이 현재 꼬리면 예외 허용)
    if next_cell == 2:
        break
    
    # 머리 전진
    snake.append((next_row, next_col))
    board[next_row][next_col] = 2

    # 사과가 아니면 이전 위치 다시 0으로 
    if next_cell!= 1:
        removed_row, removed_col = snake.popleft()
        board[removed_row][removed_col] = 0 
    
    total_move +=1
    t+=1
    if moves and moves[0][0]==t:
        time, move  = moves.popleft()
        if move == "D":
            dir_idx = (dir_idx +1)% 4
        else :
            dir_idx = (dir_idx -1) %4
    
print(total_move)

