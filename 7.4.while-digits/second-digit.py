num = int(input())
while num > 99:
    last_digit = num % 10
    num = num // 10
print(num % 10)
