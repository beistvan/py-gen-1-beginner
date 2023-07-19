n = int(input())
k = []
for _ in range(n):
    k.append(int(input()))
for i in k:
    if i < 0:
        print(i)
for i in k:
    if i == 0:
        print(i)
for i in k:
    if i > 0:
        print(i)
