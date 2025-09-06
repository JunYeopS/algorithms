case_num = int(input())

if case_num < 100:
    result = case_num
    print(result)
else:
    result = 99    # 1 - 99 확정  
    for i in range(101,case_num):
        digits = list(map(int,str(i+1)))

        a = digits[0] 
        b = digits[1]
        c = digits[2]
        if a-b == b-c:
            result += 1
    print(result)
    