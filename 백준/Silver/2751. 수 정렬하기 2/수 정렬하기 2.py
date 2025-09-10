import sys 

N = int(sys.stdin.readline())

l = []
for num in range(N):
    l.append(int(sys.stdin.readline()))    

l.sort()
for a in l:
    print(a)
