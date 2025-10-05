import sys 

input = sys.stdin.readline

n = int(input())

count = 0

if n == 3:
    print(1)
if n == 4:
    print(-1)
elif n >= 5:
    max_5 = n // 5
    for idx in range(max_5,-1,-1):
        remain = n-(idx*5)
        if remain %3 == 0:
            count = idx + remain//3
            break
    if count == 0:
        print(-1)
    else:
        print(count)
    
