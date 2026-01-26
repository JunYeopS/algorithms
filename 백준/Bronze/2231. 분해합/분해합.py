import sys 

input = sys.stdin.readline

m = int(input())

count = 0
temp = m

while temp > 0:
    count += 1
    temp //= 10

f_digit = 0
ans= 0
ls = []
for i in (range(m-(count*9), m)):
    s = i
    tem = i
    while tem > 0 :
        f_digit = tem %10
        s += f_digit
        tem //= 10
        
    if(s == m):
       ans = i
       break
        
print(ans)