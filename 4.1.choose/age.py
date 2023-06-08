n = int(input())
if n <= 13:
    print("child")
elif 14 <= n <= 24:
    print("young")
elif 25 <= n <= 59:
    print("adult")
else:
    print("old")