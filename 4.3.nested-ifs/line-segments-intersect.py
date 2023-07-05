a1, b1, a2, b2 = [int(input()) for _ in range(4)]
if b1 < a2 or b2 < a1:
    print("empty set")
elif b1 == a2:
    print(b1)
elif b2 == a1:
    print(a1)
elif a1 <= a2 < b1 < b2:
    print(a2, b1)
elif a2 <= a1 < b2 < b1:
    print(a1, b2)
elif a1 < a2 <b2 <= b1:
    print(a2, b2)
elif a2 < a1 < b1 <= b2:
    print(a1, b1)
elif a1 == a2 and b1 == b2:
    print(a1, b1)
