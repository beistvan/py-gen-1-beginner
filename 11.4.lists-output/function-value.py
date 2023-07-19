n = int(input())
x = []
for i in range(n):
    x.append(int(input()))
    print(x[i])
print()
for i in range(n):
    print(x[i] ** 2 + 2 * x[i] + 1)
