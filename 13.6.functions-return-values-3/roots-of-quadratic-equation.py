from math import sqrt

def solve(a, b, c):
    d = b * b - 4 * a * c
    x1, x2 = (-b - sqrt(d)) / (2 * a), (-b + sqrt(d)) / (2 * a)
    if x1 > x2:
        x1, x2 = x2, x1
    return x1, x2

a, b, c = int(input()), int(input()), int(input())

x1, x2 = solve(a, b, c)
print(x1, x2)
