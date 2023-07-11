num = int(input())

while num > 9:
    sum = 0
    while num > 0:
        last = num % 10
        sum += last
        num //= 10
    num = sum
print(num)
