mx = -100000000000
s = 0
for _ in range(10):
    x = int(input())
    if x < 0:
        s += x
        if x > mx:
            mx = x
if s < 0:
    print(s)
    print(mx)
else:
    print("NO")
