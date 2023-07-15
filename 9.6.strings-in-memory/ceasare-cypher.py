shf, txt = int(input()), input()
print(''.join(chr((ord(ltr) - shf - 97) % 26 + 97) for ltr in txt))
