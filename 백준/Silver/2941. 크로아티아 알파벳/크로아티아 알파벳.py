import sys

input = sys.stdin.readline

s = (input().strip())

for ch in ["dz=","z=","s=","c=","c-","d-","lj","nj"]:
    s = s.replace(ch,"*")

print(len(s))