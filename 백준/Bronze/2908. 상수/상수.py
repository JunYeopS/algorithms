l = []
case = list(map(str,input().split(' '))) #['734', '893']

for num in range(2):
    digits = list(map(str,case[num]))
    reverse_list=list(reversed(digits)) #['4', '3', '7']
    join_list = (''.join(reverse_list))
    l.append(join_list)
    
if l[0]<l[1]:
    print(l[1])
else: 
    print(l[0])
