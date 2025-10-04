n= int(input())

result = []

def hanoi_killer(n,start, mid, dst):
    if n == 0:
        return
    hanoi_killer(n-1,start,dst,mid)
    result.append((start,dst))
    hanoi_killer(n-1,mid, start,dst)
    
hanoi_killer(n,1,2,3)

print(len(result))
for a,b in result:
    print(a,b)