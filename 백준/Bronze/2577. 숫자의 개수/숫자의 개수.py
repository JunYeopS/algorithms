A, B, C = (int(input()) for _ in range(3))

mul = str(A*B*C)
a = 0;
count=[0,0,0,0,0,0,0,0,0,0]
for i,value in enumerate(mul):
    count[int(value)] += 1
for i in count:
    print(i)
    
