a, b, c = input(), input(), input()
if len(a) > len(b):
    a, b = b, a
if len(a) > len(c):
    a, c = c, a
if len(b) > len(c):
    b, c = c, b
print("YES" if (len(a) + len(c)) / 2 == len(b) else "NO")
