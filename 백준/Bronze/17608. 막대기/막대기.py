import sys

input = sys.stdin.readline

n = int(input())

stick_list = []
for i in range(n):
    stick_list.append(int(input()))

best = (stick_list[-1])

count = 1
for i in range(1,len(stick_list)+1):
    if stick_list[-i] > best:
        count +=1
        best =stick_list[-i]
    
print(count)