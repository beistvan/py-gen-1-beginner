n = int(input())
ct = 0
for _ in range(n):
    if input().count('11') >= 3:
        ct += 1
print(ct)
