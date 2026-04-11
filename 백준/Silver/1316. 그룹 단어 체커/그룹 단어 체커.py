import sys

input = sys.stdin.readline

n = int(input())
cnt = 0


for _ in range(n):
    word = list(input().strip())
    
    flag = False
    for i in range(len(word)-1):
        tmp = word[i]
            
        for j in range(i+2,len(word)): 
            if tmp != word[i+1]:
                if tmp == word[j]:
                    flag = True
                    
                    
    if not flag:
        cnt+=1

print(cnt)
                