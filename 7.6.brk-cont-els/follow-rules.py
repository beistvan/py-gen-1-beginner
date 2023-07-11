n = int(input())
k = 1
while k <= n:
    if not(k >= 5 and k <= 9 or k >= 17 and k <= 37 or k >= 78 and k <= 87):
        print(k)
    k += 1
