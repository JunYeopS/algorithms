import sys

input = sys.stdin.readline

n= input()
ls = (list(map(int,input().split())))# 4 1 5 2 3
ls.sort()
target_nums = input()
target_list = list(map(int,input().split())) #1 3 7 9 5

""" 1. start 0 , end 마지막 index -1  
    2. while 문 
    2.중간 인덱스를 찾는다 (start+end)//2 로 계속 변경
    3. 타켓과 중간을 비교 같을때 클떄 나머지 
    4. 중값이 타켓보다 크면 오른쪽 start를 mid+1 인덱스로 
"""

def is_in(list, target):
    start, end = 0, len(list)-1
    while start<=end:
        mid = (start+end)//2  # index 
    
        if list[mid] == target:
            return 1
        elif list[mid] < target:
            start = mid +1
        else:
            end = mid -1 
    return 0

for target in target_list:
    print(is_in(ls,target))