n, k, l = int(input()), int(input()), []
for i in range(n - 1):
    x = int(input())
    k += x
    l.append(k)
    k = x
print(l)
