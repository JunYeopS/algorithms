import sys 
import pprint as pp

sys.setrecursionlimit(10**6)

preorder = list(map(int, sys.stdin.read().split()))

# print(preorder) #[50, 30, 24, 5, 28, 45, 98, 52, 60]

def postorder(start,end):
    if start>end: 
        return    
    root = preorder[start]

    next = start +1 
    while next <= end and preorder[next]< root:
        next += 1

    # 왼쪽 서브트리
    postorder(start+1, next-1)
    # 오른쪽 서브트리
    postorder(next, end)
    print(root)
    
postorder(0,len(preorder)-1)
