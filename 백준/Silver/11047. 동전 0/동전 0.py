import sys 

n, k = map(int,input().split())

wallet = []
for _ in range(n):
    currency = int(input())
    wallet.append(currency)

#최솟값이니까 큰 지폐부터 써야 한다    
wallet.reverse()

count = 0 

for currency in wallet:
    if currency <= k:
        while currency <= k:
            # 몫은 몇번 쓸수 있는지를 
            count_with_cur_currency = k//currency
            # 나머지는 쓰고 남은 금액 
            k = k%currency
            count += count_with_cur_currency
print(count)