n = input()

count_3 = 0
count_last_digit = 0
count_even = 0
sum_greater_than_5 = 0
product_greater_than_7 = 1
found_greater_than_7 = False
count_0_and_5 = 0

last_digit = n[-1]

for i in range(len(n)):
    digit = int(n[i])

    if digit == 3:
        count_3 += 1

    if n[i] == last_digit:
        count_last_digit += 1

    if digit % 2 == 0:
        count_even += 1

    if digit > 5:
        sum_greater_than_5 += digit

    if digit > 7:
        product_greater_than_7 *= digit
        found_greater_than_7 = True

    if digit == 0 or digit == 5:
        count_0_and_5 += 1

if not found_greater_than_7:
    product_greater_than_7 = 1

print(count_3)
print(count_last_digit)
print(count_even)
print(sum_greater_than_5)
print(product_greater_than_7)
print(count_0_and_5)
