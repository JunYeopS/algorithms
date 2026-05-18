T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    num = input()

    if num == "...":
        print("...")
        break
    
    N,M = map(int,num.split())
    
    matrix = []
    sum = 0
    highest = 0 
    for _ in range(N):
        matrix.append(list(map(int,input().split())))
        
    for i in range(N-M+1):
        for j in range(N-M+1):
            
            for idx in range(i,i+M):
                for jdx in range(j,j+M):
                    sum += matrix[idx][jdx]
                
            if sum > highest:
                highest = sum
            sum = 0
    
    print(f"#{test_case} {highest}")