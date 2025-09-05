A = int(input())
B = int(input())

B_digits = list(map(int,str(B)))
     
print(A * B_digits[-1])
print(A * B_digits[-2])
print(A * B_digits[-3])
print(A * B)
