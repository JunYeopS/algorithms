N = input()

case = list(map(int,input().split()))

prime_list = []
for i in case:
    if i>1:
        # print(i)
        count = 0
        for idx in range(1,i+1):
            if i%idx == 0:
                count +=1
        if count==2:
            prime_list.append(i)                        
print(len(prime_list))
    