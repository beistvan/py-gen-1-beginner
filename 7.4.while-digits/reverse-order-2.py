num = int(input())
st = ""
while num != 0:
    last_digit = num % 10
    st += str(last_digit)
    num = num // 10
print(st)
