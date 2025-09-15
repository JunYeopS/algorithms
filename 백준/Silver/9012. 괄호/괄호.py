import sys

input = sys.stdin.readline

n = int(input())

def is_empty(list):
    if len(list) ==0:
        return True
    else:
        return False
        
for i in range(n):
    ls = []
    case = list(input().strip())
    
    for i in case: 
        if i== '(':
            ls.append(i)
        elif i == ')':
            if is_empty(ls) == True:
                ls.append(i)
            else:
                if is_empty(ls) == False:
                    if ls[-1] == '(':
                        ls.pop()

    if len(ls) == 0:
        print("YES")
    else: 
        print("NO")