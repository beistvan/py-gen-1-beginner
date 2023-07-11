num = int(input())
minimum = 10
maximum = -1
while num != 0:
    last_digit = num % 10
    if last_digit > maximum:
        maximum = last_digit
    if last_digit < minimum:
        minimum = last_digit
    num = num // 10
print("Max digit is", maximum)
print("Min digit is", minimum)
