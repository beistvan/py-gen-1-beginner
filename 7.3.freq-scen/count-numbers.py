a, b = int(input()), int(input())
c = 0
for i in range(a, b + 1):
    if i**3 % 10 == 4 or i **3 % 10 == 9:
        c += 1
print(c)
