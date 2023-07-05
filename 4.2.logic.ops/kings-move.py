a, b, c, d = [int(input()) for _ in range(4)]
print("YES" if abs(a - c) == 1 and b == d or abs(b - d) == 1 and a == c or abs(a - c) == 1 and abs(b - d) == 1 else "NO")
