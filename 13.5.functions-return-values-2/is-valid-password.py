from sympy import isprime

def is_valid_password(password):
    if password.count(':') > 2:
        return False
    a, b, c = password.split(':')
    return str(a) == str(a)[::-1] and isprime(int(b)) and int(c) % 2 == 0

psw = input()

print(is_valid_password(psw))
