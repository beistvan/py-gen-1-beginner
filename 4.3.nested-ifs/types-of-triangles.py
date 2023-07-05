a, b, c = int(input()), int(input()), int(input())
print("Equilateral" if a == b == c else "Isoceles" if a == b or b == c or c == a else "Scalene")
