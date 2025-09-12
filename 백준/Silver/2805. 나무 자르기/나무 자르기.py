import sys

input = sys.stdin.readline

n,m = map(int,input().split())
trees = list(map(int,input().split()))

def tree_cutter(trees, m):
    start, end = 0 , max(trees)
    lis = []
    while start <= end:
        total = 0
        mid = (start+end)//2
        for a in trees:
            if a > mid:           # mid보다 큰 나무만 자른다
                total += a - mid
        if total >= m:
            start = mid +1
            lis.append(mid)
        else :
            end = mid -1     
    return max(lis)
print(tree_cutter(trees,m))
                     