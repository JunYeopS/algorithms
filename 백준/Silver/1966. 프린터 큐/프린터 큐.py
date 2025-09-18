import sys 
input = sys.stdin.readline

n = int(input())

# 제일 먼저 나오는건 높은게 먼저 나와야 하고 
# 아니면 다시 넣는다 
# 높은 first out 을 갱신 시켜서 타켓이랑 인덱스랑 같으면 그때 print(count)

for _ in range(n):
    nums,target =map(int,input().split())
    waiting_ls = list(map(int,input().split()))
    count = 0    
    while True:
        first_out = max(waiting_ls)
        x = waiting_ls.pop(0)  # 맨 앞 꺼내기
        if x != first_out:    # 우선 순위 가장 안높아? 
            waiting_ls.append(x)  # 맨 뒤로 보내기
        else:
            count += 1
            if target == 0:
                print(count)
                break
        target = (target - 1) % len(waiting_ls)  # 인덱스 갱신