a = int(input())
b = int(input())
if b < a:
    b = a + b
    a = b - a
    b = b - a

c = 0
max = 0
num = 0
for i in range(a, b + 1):
    c = 0
    for k in range(1, i + 1):
        if i % k == 0:
            c += k
    if max <= c:
        max = c
        num = i
print(num, max)
