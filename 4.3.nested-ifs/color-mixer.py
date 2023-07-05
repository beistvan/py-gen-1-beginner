a, b = input(), input()
c = {"red", "blue", "yellow"}
if c.union({a, b}) != c:
    print("color error")
elif a == b:
    print(a)
elif a == "red" and b == "blue" or b == "red" and a == "blue" :
    print("violet")
elif a == "red" and b == "yellow" or b == "red" and a == "yellow":
    print("orange")
elif a == "yellow" and b == "blue" or b == "yellow" and a == "blue":
    print("green")