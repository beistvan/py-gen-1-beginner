n = int(input())
if 0 <= n <= 36:
    if n == 0:
        print("green")
    elif (0 < n < 11 or 18 < n < 29) and n % 2 == 1 or (10 < n < 19 or 28 < n < 37) and n % 2 == 0:
        print("red")
    else:
        print("black")
else:
    print("invalid input")