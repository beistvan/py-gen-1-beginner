def fact(n):
    return 1 if n == 0 else n * fact(n - 1)
n = int(input())
print(sum(fact(i) for i in range(1, n + 1)))
