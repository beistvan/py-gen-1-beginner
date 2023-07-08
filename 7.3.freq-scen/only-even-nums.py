cnt = 0
for _ in range(10):
    if int(input()) % 2 == 0:
        cnt += 1
print('YES' if cnt == 10 else 'NO')
