x_axis,y_axis= (map(int,input().split())) 

cut_num = int(input()) 

x_list = [0]
y_list = [0]
 
x_list.append(y_axis)
y_list.append(x_axis)
dif_x = 0
dif_y = 0
for case in range(cut_num):
    
    cut = list(map(int,input().split()))
    x = cut[0]
    y = cut[1]
     
    if x == 0: 
        x_list.append(y)
    else:
        y_list.append(y)
    
x_list.sort() 
y_list.sort()   
    
for i in range(len(x_list)-1):
    a = x_list[i+1] - x_list[i]  
    if a > dif_x:
        dif_x = a
for j in range(len(y_list)-1):
    b = y_list[j+1] - y_list[j]
    if b > dif_y:
        dif_y = b

print(dif_x*dif_y)    