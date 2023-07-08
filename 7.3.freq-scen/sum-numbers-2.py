print(sum((i if i**2 % 10 in [2, 5, 8] else 0 for i in range(1, int(input()) + 1))))
