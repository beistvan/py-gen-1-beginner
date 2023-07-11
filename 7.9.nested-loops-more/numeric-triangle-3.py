n = int(input())
k = 1
for i in range(n):
    for j in range(i + 1):
        print(str(k) + " ", end="")
        k += 1
    print()
