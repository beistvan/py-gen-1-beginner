a, b, c, d = [int(input()) for _ in range(4)]
print("YES" if a == c and b != d or b == d and a != c else "NO")
