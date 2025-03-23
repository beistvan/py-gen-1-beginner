import re

def check_number(number: str) -> str:

    pattern = r'^[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}_(\d{2}|\d{3})$'

    if re.match(pattern, number):
        return "YES"
    else:
        return "NO"

number = input().strip()

print(check_number(number))
