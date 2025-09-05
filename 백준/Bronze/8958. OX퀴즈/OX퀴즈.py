test_cases = int(input())

for case in range(test_cases):
    case = input()
    total_score = 0
    count = 0
    for i in case:
        if i == 'O':
            count +=1
            total_score += count
        else:   
            count = 0
    print(total_score)