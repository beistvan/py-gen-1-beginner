print(*(int(p)**2 for p in input().split() if int(p) % 2 == 0 and int(p)**2 % 10 != 4), end=' ')
