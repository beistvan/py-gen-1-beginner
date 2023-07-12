s = input()
c = "No digits"
for i in range(len(s)):
    if s[i] in '0123456789':
        c = "Digit"
        break
print(c)
