a = int(input())
b = int(input())
if a == 1:
    a = 2
for i in range(a, b + 1):
    is_prime = True
    j = 2
    while j * j <= i:
        if i % j == 0:
            is_prime = False
            break
        j += 1
    if is_prime:
        print(i)
