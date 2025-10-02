import sys 

input = sys.stdin.readline

n = int(input())

count = 0 

if n <=1 or n == 3:
    count=-1
else:
    max_count_5 = n // 5
    remain = n % 5
    # 5원짜리 맥스 count 부터 하나씩 줄여가면서
    # 2로 나눠지면 가능
    while remain % 2 != 0 and max_count_5 > 0:
        max_count_5 -= 1
        # 5원 덜고 남은 돈은 + 5 
        remain += 5
    count = (max_count_5 + remain // 2)

print(count)