import sys
input = sys.stdin.readline
"""
집 좌표 정렬 → 거리 d를 1부터 (최대좌표-최소좌표) 사이에서 이진 탐색
주어진 d에 대해 왼쪽부터 거리 ≥ d가 될 때마다 하나씩 배치해서 개수 세기
배치 수 ≥ C면 d를 키우고, 아니면 줄이기 → 가장 큰 d를 답으로 선택
"""
N, C = map(int,input().split()) 

houses = list(map(int, sys.stdin.read().split()))

houses.sort() #1,2,4,8,9
def binary_search(houses,C):
    start, end = 1, houses[-1]-houses[0]  #거리를 이진으로 (최소 거리 1 부터 최대거리인 첫인덱스와 마지막 인덱스의 차이)
    d=0
    while start<=end:
        mid = (start+end)//2
        count = 1
        last = houses[0]
        for x in houses[1:]:
            if x - last >= mid:
                count += 1
                last = x
        if count >= C:
            start = mid +1
            d = mid
        else:
            end = mid - 1
    return d
        
print(binary_search(houses,C))

