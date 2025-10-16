import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
targets = list(map(int, input().split()))

dq = deque(range(1, N + 1))
ops = 0

for x in targets:
    idx = dq.index(x)
    if idx <= len(dq) // 2:
        # 왼쪽 회전 idx번
        dq.rotate(-idx)
        ops += idx
    else:
        # 오른쪽 회전 len-idx번
        r = len(dq) - idx
        dq.rotate(r)
        ops += r
    dq.popleft()  # 3번 연산(맨 앞 pop)

print(ops)
