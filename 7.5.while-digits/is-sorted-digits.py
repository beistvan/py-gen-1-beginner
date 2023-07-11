num = int(input())
k = num % 10
num = num // 10
answer = "YES"
while num > 0:
    last_digit = num % 10 
    if k > last_digit:
        answer = "NO"
    k = last_digit
    num = num // 10
print(answer)
