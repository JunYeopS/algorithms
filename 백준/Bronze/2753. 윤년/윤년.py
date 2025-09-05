year = int(input())
    
if (1<= year <=4000):
    print(int((year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)))
