a, b, c = input(), input(), input()
if len(a) > len(b):
    a, b = b, a
if len(a) > len(c):
    a, c = c, a
if len(b) > len(c):
    b, c = c, b
print(a, c, sep='\n')
