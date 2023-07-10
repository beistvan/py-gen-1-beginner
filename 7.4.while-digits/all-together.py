num = int(input())
total = 0
amount = 0
product = 1
average = 0
lastDigit = -1
while num != 0:
    last_digit = num % 10
    total += last_digit
    amount += 1
    product *= last_digit
    if lastDigit == -1:
        lastDigit = last_digit
    num = num // 10
average = total / amount
firstDigit = last_digit
print(total)
print(amount)
print(product)
print(average)
print(firstDigit)
print(firstDigit + lastDigit)
