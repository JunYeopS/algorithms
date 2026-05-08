c = 0
for idx in range(1,11):
    T = input()
    
    if T == "...":
        print("...")
        break
    
    ls = list(map(int, input().split()))
    ans = 0
    
    i = 2
    flag = False
    while i <= len(ls)-3:        
        
        tmp = ls[i]
        # 오른쪽  
        if tmp > ls[i+1]:
            if tmp > ls[i+2]:
                # 왼쪽 
                if tmp > ls[i-1]:
                    if tmp > ls[i-2]:
                        higher = max(ls[i-1],ls[i-2],ls[i+1],ls[i+2])
                        ans = ans + tmp - higher
                        i += 2
        i+=1
        
    c += 1
    print(f"#{c} {ans}")
