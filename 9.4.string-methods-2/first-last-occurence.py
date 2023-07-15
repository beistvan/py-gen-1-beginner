s = input()
if s.count('f') == 1:
    print(s.index('f'))
elif s.count('f') >= 2:
    print("%d %d"%(s.index('f'), s.rindex('f')))
else:
    print("NO")
