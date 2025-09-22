import sys 

input= sys.stdin.readline

st_ls = list(input().strip()) 

bomb_ls = list(input().strip())

# 일단 넣고 밤 리스트 만큼 슬라이싱 해서 비교? 
# 같으면 그만 큼 팝팝팝팝 

result = []
for i in st_ls:
    result.append(i)
    # result 길이가 bomb 길이 이상일 때만 비교
    if len(result) >= len(bomb_ls):
        if result[-len(bomb_ls):] == bomb_ls: #밤 길이 만큼 슬라이싱 해서 비교햐 
            for _ in range(len(bomb_ls)):
                result.pop()
if result : 
    print("".join(result))
else:
    print("FRULA")