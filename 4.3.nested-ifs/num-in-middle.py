a, b, c = int(input()), int(input()), int(input())
print(b if a <= b <= c or c <= b <= a else a if b <= a <= c or c <= a <= b else c)
