s = input().split()
for w in s:
    l = sum(map(str.isalpha, w))
    enc, shf = '', l
    for c in w:
        if c.isalpha():
            if c.isupper():
                enc += chr((ord(c) + shf - ord('A')) % 26 + ord('A'))
            else:
                enc += chr((ord(c) + shf - ord('a')) % 26 + ord('a'))
        else:
            enc += c
    print(enc, end=' ')
