a, b, c = int(input()), int(input()), input()
print("Division by zero!" if b == 0 and c == "/" else "Invalid operation" if c not in ["+","-","*","/"] else eval(f"{a}{c}{b}"))
