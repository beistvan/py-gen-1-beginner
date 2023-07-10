num = int(input())
k = num % 10
answer = "YES"
while num > 0:
    last_digit = num % 10
    if last_digit != k:
        answer = "NO"
    num = num // 10
print(answer)
