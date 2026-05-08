c = 0
for idx in range(1,11):
    T = input()
    
    if T == "...":
        print("...")
        break
    
    ls = list(map(int, input().split()))
    ans = 0
    
    i = 2
    while i <= len(ls)-3:        
        
        tmp = ls[i]

        higher = max(ls[i-1],ls[i-2],ls[i+1],ls[i+2])
        if higher < tmp :
            ans = ans + tmp - higher
            i += 3
        else:
            i+=1
        
    c += 1
    print(f"#{c} {ans}")