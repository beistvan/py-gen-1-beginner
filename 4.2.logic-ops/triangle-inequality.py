a, b, c = int(input()), int(input()), int(input())
print("YES" if a + b > c and b + c > a and c + a > b else "NO")
