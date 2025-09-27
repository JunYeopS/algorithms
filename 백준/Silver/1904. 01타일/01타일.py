import sys
input = sys.stdin.readline

n = int(input())
c= 0
a,b = 1, 2

if n == 1:
    print(1)
if n == 2:
    print(2)    
if n >= 3 : 
    for i in range(2,n,1):
        c = (a + b) %15746 
        a = b 
        b = c 
    print(c)