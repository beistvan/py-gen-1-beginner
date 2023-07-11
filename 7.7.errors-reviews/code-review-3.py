s = 0
for i in range(7):
    n = int(input())
    if n % 2 == 0:
        s = s + n
print(0 if s == 0 else s)
