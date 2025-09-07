n = int(input()) 

best = ((2**n)-1)

print(best)
def hanoi_killer (n,A,B,C):
    if n == 0 or n >20:
        return
    hanoi_killer(n-1,A,C,B)
    print(A,C)
    hanoi_killer(n-1,B,A,C)
    
(hanoi_killer(n,"1","2","3"))
