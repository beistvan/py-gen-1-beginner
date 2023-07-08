n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(1, 1)
else:
    f1 = f2 = 1
    print(1, 1, sep=" ", end=" ")
    for _ in range(n - 2):
        f = f1 + f2
        f2 = f1
        f1 = f
        print(f, sep=" ", end=" ")
