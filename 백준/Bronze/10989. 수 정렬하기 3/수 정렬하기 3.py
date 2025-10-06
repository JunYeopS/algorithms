import sys 

input = sys.stdin.readline

n = int(input())

nums = [0] *(10001)

for i in range(n):
    num = int(input())
    nums[num] +=1 

for idx in range(len(nums)):
    if nums[idx]>0:
        for _ in range(int(nums[idx])):
            print(idx)