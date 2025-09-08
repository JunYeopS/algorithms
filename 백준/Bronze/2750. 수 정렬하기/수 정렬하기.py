N = int(input())

l = []
for num in range(N):
    l.append(int(input()))    
    
def bubble_sort(l):
    if len(l)>1000:
        return
    
    for i in l:
        for j in (range(len(l)-1)):
            if l[j]>l[j+1]:
                l[j] ,l[j+1] = l[j+1],l[j]
            else:
                continue
    
    for a in l:
        print(a)

bubble_sort(l)