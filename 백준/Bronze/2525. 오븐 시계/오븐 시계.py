import sys

input = sys.stdin.readline

cur_time = list(map(int,input().split(" ")))

c = int(input())

cur_time[1] += c 

if cur_time[1] >= 60:
    re_h = cur_time[1] // 60
    re_m = cur_time[1] - (re_h*60)
    cur_time[0] += re_h
    cur_time[1] = re_m
if (cur_time[0])>=24:
    cur_time[0] -= 24

print(*cur_time)