n = int(input())
for i in range(1, n + 1):
    for j in range(1, (2 * i) // 2 + 1):
        print(j, sep='', end='')
    for j in range((2 * i) // 2 - 1, 0, -1):
        print(j, sep='', end='')
    print()
