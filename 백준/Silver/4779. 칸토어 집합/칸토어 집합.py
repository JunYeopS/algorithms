def cantor_killer(start, length):
    if length == 1:
        return
    third = length//3
    for i in range(start+third,start + 2*third):
        ls[i] =' '
    cantor_killer(start, third)
    cantor_killer(start + 2*third,third)
    
while True:
    try:
        n =  int(input())
        ls = ['-']*(3**n)
        cantor_killer(0,len(ls))
        print("".join(ls))
    except:
        break