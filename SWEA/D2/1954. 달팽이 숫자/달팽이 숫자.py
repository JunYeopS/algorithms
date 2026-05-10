T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    # 우 하 좌 상 
    dx = [0, 1, 0, -1]                                                                     
    dy = [1, 0, -1, 0]
    x, y, dir = 0, 0, 0
      
    for num in range(1,n*n+1):
        
        matrix[x][y] = num
        nx,ny = x + dx[dir], y + dy[dir]
                        
        if not(0 <= nx < n and 0 <= ny < n) or matrix[nx][ny] != 0:
            dir = (dir+1) % 4
            nx = x + dx[dir]
            ny = y + dy[dir]   
        x,y =nx,ny
    
    print(f"#{test_case}")
    for _ in range(n):
        print(*matrix[_])