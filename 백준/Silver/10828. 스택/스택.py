import sys 

input = sys.stdin.readline

n = int(input())

ls = []
for i in range(n):
    method = (input().split())
    if len(method) == 2:
        ls.append(int(method[1]))
    elif method[0] == "top":
        if len(ls) >=1:    
            print(ls[-1])
        else: 
            print(-1)
    elif method[0]== "size":
        print(len(ls))
    elif method[0] == "empty":
        if len(ls) == 0:
            print(1)
        else :
            print(0)
    else: #pop
        if len(ls) >= 1:
            a= ls.pop()
            print(a)
        else: 
            print(-1)