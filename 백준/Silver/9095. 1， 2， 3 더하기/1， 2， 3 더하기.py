cases = int(input())

def count(n):
    if n == 0:
        return 1
    if n < 0:
        return 0   
    
    return count(n-1)+count(n-2)+count(n-3)

for case in range(cases):
    print(count(int(input())))
    