def is_password_good(password):
    count = 0
    if len(password) >= 8:
        count += 1
    if password != password.upper():
        count += 1
    if password != password.lower():
        count += 1
    for i in password:
        if i.isnumeric():
            count += 1
            break
    return count == 4

txt = input()

print(is_password_good(txt))
