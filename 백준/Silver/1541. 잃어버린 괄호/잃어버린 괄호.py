import sys 

input= sys.stdin.readline
expression = input().strip()

# '-' 기준으로 쪼갬
sub_ls = expression.split('-')

# 첫 번째 조각은 그냥 더하기
first = sum(map(int, sub_ls[0].split('+')))

# 나머지는 모두 합쳐서 빼기
others = 0
for p in sub_ls[1:]:
    others += sum(map(int, p.split('+')))

print(first - others)

