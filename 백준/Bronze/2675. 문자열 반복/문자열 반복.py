cases_num = int(input())

for i in range(cases_num):
    case = list(map(str,input().replace(' ',"")))
    
    R = int(case.pop(0))

    result = ''
    for idx in case:
        result += idx * R
    print(result)    

