s = input()
k = 0
c = ''
for a in s:
    if s.count(a) >= k:
        k = s.count(a)
        c = a
print(c)
