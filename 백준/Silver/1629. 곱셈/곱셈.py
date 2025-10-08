import sys 

input= sys.stdin.readline

A,B,C = (map(int,input().split()))

def fast_mul(a,b,c):
    
    if b == 0:
        return 1
    split = fast_mul(a, b // 2, c)
    split = split * split % c

    if b % 2 == 0:
        return split
    else:
        return (split * a) % c
    
print(fast_mul(A,B,C))

