n = int(input())

num = n 
count = 0
while  True:
    
    ten = num // 10 
    one = num %10   
    sum = ten+one
    if sum >=10:
        sum = (ten+one) -10
    num = (one*10) +sum
    
    count +=1
    
    if num == n:
        print(count)
        break