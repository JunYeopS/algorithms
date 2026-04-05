import sys

input = sys.stdin.readline

s = list(input().strip())

count = 0
for i in range(len(s)):
    if s[i] == '=':
        count -= 1
        if s[i-2] == 'd' and s[i-1] == 'z':
            count -=1 
    elif s[i] == '-':
        count -= 1
    elif s[i] == 'j':
        if s[i-1] == 'l' or s[i-1] == 'n':
            count -= 1
    count +=1 
    
print(count)