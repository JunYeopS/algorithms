import sys
s = sys.stdin.readline().strip()

if len(s) >= 2 and s[:2] == "0x":
    print(int(s, 16))
elif len(s) >= 2 and s[0] == "0":
    print(int(s, 8))
else:
    print(int(s, 10))
