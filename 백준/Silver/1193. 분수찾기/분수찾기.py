import sys

input = sys.stdin.readline

target = int(input())
seq_num = 0
top, bot = 0,0

for i in range(1,target+1):
    seq_num += i 
    
    if seq_num >= target:
        seq_num -= i

        offset = target - seq_num

        if i % 2 == 0:
            top = offset
            bot = i + 1 - offset
        else:
            top = i + 1 - offset
            bot = offset
        break

print(f"{top}/{bot}")
    
