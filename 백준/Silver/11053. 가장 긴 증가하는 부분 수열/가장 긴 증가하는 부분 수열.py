import sys 

input= sys.stdin.readline

n = int(input())

ls = list(map(int,input().split()))

dp=[1]*(n)

for i in range(n):           # i번째 원소를 기준으로
    for j in range(i):       # i보다 앞에 있는 원소들을 모두 확인
        if ls[j] < ls[i]:    # 증가하는 조건이라면
            # dp[i]는 이전 j에서 끝나는 LIS에 ls[i]를 붙였을 때와 현재 dp[i] 중 큰 값 선택
            dp[i] = max(dp[i], dp[j] + 1)             
print(max(dp))
