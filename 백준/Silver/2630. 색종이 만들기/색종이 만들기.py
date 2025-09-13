import sys
input = sys.stdin.readline

size = int(input())

paper = []
for _ in range(size):
    row = list(map(int,input().split()))
    paper.append(row)

"""
    1. 분할정복 Top down방식을 활용한 재귀 문제 
    2. 전체 영역 검사 
    3. 색이 다 같으면 -> 개수 +1 
    4. 아니면 size 반으로 나눈다 
"""

blue= 0
white = 0

def paper_cut (x,y, size):
    global blue,white
    color = paper[x][y]
    if size ==1:
            if color == 1:
                blue+=1
            else:
                white +=1
            return 
     
    if scan_all(x,y,size) == False:
        paper_cut(x, y, size//2) #왼쪽 위 
        paper_cut(x, y+size//2, size//2) # 오른쪽 위 
        paper_cut(x+size//2, y, size//2) # 왼쪽 아래
        paper_cut(x+size//2, y+size//2, size//2) # 오른쪽 아래 
    else:
        if color == 1:
            blue +=1
        else:
            white +=1
        return 

##전체 영역 검사
def scan_all(x,y,size):
    color = paper[x][y]
    for i in range(x, x+size):
        for j in range(y,y+size):
            if paper[i][j] != color:
                return False
    return True

paper_cut(0,0,size)
print(white)
print(blue)
