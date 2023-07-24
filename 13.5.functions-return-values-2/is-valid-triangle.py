def is_valid_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

a, b, c = int(input()), int(input()), int(input())

print(is_valid_triangle(a, b, c))
