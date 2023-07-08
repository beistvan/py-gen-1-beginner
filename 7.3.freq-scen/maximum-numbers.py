n, max1, max2 = int(input()), -1, -1
for _ in range(n):
    k = int(input())
    if k > max1:
        max2 = max1
        max1 = k
    elif k > max2:
        max2 = k
print(max1, max2, sep='\n')
