def solution(m, n, startX, startY, balls):
    answer = []
    
    for x, y in balls:
        ans = []
        dis = []
        
        left = [-x, y]
        right = [2 * m - x, y]
        down = [x, -y]
        up = [x, 2 * n - y]

        if not (startY == y and startX > x):
            dis.append(left)
        if not (startY == y and startX < x):
            dis.append(right)
        if not (startX == x and startY > y):
            dis.append(down)
        if not (startX == x and startY < y):
            dis.append(up)

        for i in range(len(dis)):
            
            distance = (dis[i][0] - startX) ** 2 + (dis[i][1]-startY) **2 
            
            ans.append(distance)
        answer.append(min(ans))
    
    return answer