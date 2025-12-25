n = int(input())
s = input()

total = 0
current = ""

for ch in s:
    if ch.isdigit():
        current += ch
    else:
        if current:
            total += int(current)
            current = ""

if current:
    total += int(current)

print(total)
