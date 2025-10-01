import sys 
import pprint as p
input = sys.stdin.readline

n = int(input())

schedule = []
for _ in range(n):
    start_t,end_t = list(map(int,input().strip().split()))
    schedule.append((end_t,start_t))

#그리디의 핵심은 정렬을 얼마나 잘 했냐 
#종료 시간이 빠른 순서로 정렬 
schedule.sort()
# p.pp(schedule)
#가장 빨리 끝나는 회의로 시작 
count = 1
end_t = schedule[0][0]

if len(schedule) > 2:
    for i in range(1,len(schedule)):
        #종료 시간 보다 시간 시간이 같거나 커야지만 한다 
        if end_t <= schedule[i][1]:
            end_t = schedule[i][0]
            count +=1
else:
    if len(schedule)==2:
        if end_t <= schedule[1][1]:
            count +=1
            
print(count)