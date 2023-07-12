s = input()
a = p = 0
for i in s:
    if i == '+':
        a += 1
    if i == '*':
        p += 1
print(f"Character + occurs {a} times")
print(f"Character * occurs {p} times")
