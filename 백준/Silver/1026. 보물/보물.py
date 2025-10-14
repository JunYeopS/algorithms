n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A는 오름차순, B는 내림차순
A.sort()
B.sort(reverse=True)

# 최소합 계산
S = sum(A[i] * B[i] for i in range(n))

print(S)
