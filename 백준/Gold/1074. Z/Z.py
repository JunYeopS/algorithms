n,r,c = map(int,input().split())

def Z(n,r,c,quad):
    
    if n == 0:
        return 0
    
    half = (2**(n-1))
    quad = 0
    ans = 0 
    if r < half and c < half:  # 왼쪽 위
        quad += 0
        ans += quad * (half*half)
        return ans + Z(n-1, r,c ,quad)
    elif r < half and c >= half:  # 오른쪽 위 
        quad += 1
        ans += quad * (half*half)
        return ans + Z(n-1, r,c-half, quad) 
    elif r >= half and c < half:    # 왼쪽 아래
        quad += 2
        ans += quad * (half*half)
        return ans + Z(n-1, r-half, c, quad)  
    elif r >= half and c >= half:    # 오른쪽 아래 
        quad += 3 
        ans += quad * (half*half)
        return ans + Z(n-1, r-half, c-half, quad)

print(Z(n,r,c,0))