import sys

input = sys.stdin.readline

n = int(input())

solution_list = list(map(int, input().split()))

solution_list.sort() #[-99, -2, -1, 4, 98]


"""
total < 0면 합을 0에 더 가깝게 키우기 위해 left += 1
total > 0면 합을 줄이기 위해 right -= 1
total == 0이면 바로 정답(가장 최적) 
"""

def print_greater(x,y):
    if x > y:
        print(y,x)
    else:
        print(x,y)
    

left, right = 0, len(solution_list)-1
x,y =0,0
best = float('inf')
while left<right: 
    
    total =solution_list[left]+solution_list[right]
    
    if abs(total) < best: 
        best = abs(total)
        x,y = solution_list[left],solution_list[right]
    
    if total == 0:
        print_greater(solution_list[left],solution_list[right])
        break
    if total < 0: 
        left +=1 
    else:
        right -=1        
print_greater(x,y)
    