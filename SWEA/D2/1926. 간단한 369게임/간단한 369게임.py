T = int(input())
                                                                                        
ls = []                                                                                
for i in range(1, T+1):
    count = 0
    for d in str(i):                                                                     
        if d in ('3', '6', '9'):
            count += 1                                                                   
                                                                                        
    if count == 0:
        ls.append(i)
    else:                                                                                
        ls.append('-' * count)
                                                                                        
print(*ls)   