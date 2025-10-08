import sys 

input = sys.stdin.readline

n = int(input())

cnt_0= [1, 0, 1]
cnt_1= [0, 1, 1]

for i in range(3,41):
    cnt_0.append(cnt_0[i-1]+cnt_0[i-2])
    cnt_1.append(cnt_1[i-1]+cnt_1[i-2])
    
for _ in range(n):
    target = int(input())
    print(cnt_0[target],cnt_1[target])