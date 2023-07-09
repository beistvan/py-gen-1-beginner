n = int(input())
p = [25, 10, 5, 1]
k = 0
for m in p:
    while n >= m:
        k += 1
        n -= m
print(k)
