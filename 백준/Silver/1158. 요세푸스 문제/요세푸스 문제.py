import sys
input = sys.stdin.readline

n, k = map(int, input().split())

table = [i for i in range(1, n+1)]
ans = []

idx = 0  # 0-index 기준 시작 위치
while table:
    idx = (idx + k - 1) % len(table)  # k번째 사람의 인덱스
    ans.append(table.pop(idx))        # 제거하면서 정답에 추가

print("<" + ", ".join(map(str, ans)) + ">")
