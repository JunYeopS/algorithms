import sys 

input = sys.stdin.readline

a_num,b_num = map(int,input().split())

a_list = set(list(map(int,input().split())))

b_list = set(list(map(int,input().split())))

# a 에서 b와 교집합인것들 뺸다 
# b에서 똑같이 
# 각 갯수를 더한다 

count = 0 
for i in a_list:
    if i in b_list:
        continue
    else:
        count +=1 

for i in b_list:
    if i in a_list:
        continue
    else:
        count +=1
        
print(count)