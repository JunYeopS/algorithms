def solution(board, h, w):
    answer = 0
    n = len(board)
    
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    for i in range(4):
        check_x = dx[i] + h
        check_y = dy[i] + w
        
        if 0 <= check_x < n and 0 <= check_y < n:
            if board[check_x][check_y] == board[h][w]:
                answer+=1
    
    return answer