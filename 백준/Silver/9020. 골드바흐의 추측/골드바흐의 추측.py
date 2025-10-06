import sys 

input = sys.stdin.readline

n = int(input())

is_prime = [True] * (10001)
is_prime[1] = False

prime_range = int(len(is_prime)**(1/2))

for i in range(2,prime_range+1):
    if not is_prime[i]:
        continue
    for j in range(i*2,len(is_prime),i):
        is_prime[j] = False

for _ in range(n):
    target = int(input())
    for i in range(target//2,0,-1):
        if is_prime[i] and is_prime[target - i]:
                print(i, target-i) 
                break
