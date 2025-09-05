test_cases= int(input())

for i in range(test_cases):
    case = list(map(int,input().split()))
    
    scores = case.pop(0)
    
    avg_score = ((sum(case)/scores))
    count = 0
    for score in case:
        if (score>avg_score):
            count += 1
    greater_rate = (count/scores)*100
    rate = round(greater_rate,3)
    print(f'{rate:.3f}%')
