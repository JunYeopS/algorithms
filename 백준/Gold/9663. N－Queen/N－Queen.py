n = int(input())

column_used = [False] * n
diagosis_up = [False] * (2 * n -1)
diagosis_down = [False] * (2 * n -1)
count = 0
def N_queen_killer(row):
    global count,n
    if row == n:
        count+=1
        return
    
    for col in range(n):
        if (column_used[col]) or (diagosis_up[(n-1)-(row - col)]) or (diagosis_down[row +col]) :
            continue
        column_used[col] = True 
        diagosis_down[row +col]= True
        diagosis_up[(n-1)-(row - col)] = True
        N_queen_killer(row+1)
        column_used[col] = False
        diagosis_down[row + col]= False
        diagosis_up[(n-1)-(row - col)] = False

N_queen_killer(0)
print(count)
    