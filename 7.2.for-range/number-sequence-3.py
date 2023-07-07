m, n = int(input()), int(input())
for i in range(m + m % 2 - 1, int(-(m - n + 1) / 2 * 2 + m + 1) - 1, -2):
    print(i)
