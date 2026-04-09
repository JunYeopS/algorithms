import sys

input = sys.stdin.readline

ls = []
ans = []

for i in range(5):
        ls.append(list(input().strip()))

for i in range(5):
    l = 15 - len(ls[i])
    ls[i] += ("*" for _ in range(l))
    
for i in range(15):
    for j in range(5):
        if not ls[j][i] == '*':
            ans.append(ls[j][i])
        else: 
            continue

print("".join(ans))