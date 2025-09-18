import sys 

input= sys.stdin.readline

n = int(input())

s_cards = list(map(int,input().split()))

m = int(input())

check_cards = list(map(int,input().split()))

result =[]
s_cards.sort()

for target in check_cards:
    start, end = 0, len(s_cards)-1
    founded= False
    while start <=end:
        mid = (start+end)//2

        if  s_cards[mid] == target: 
            result.append(1)
            founded=True
            break
        elif s_cards[mid]> target:
            end = mid -1    
        else:
            start = mid +1 
    if founded== False:
        result.append(0)    
    
print(*result)