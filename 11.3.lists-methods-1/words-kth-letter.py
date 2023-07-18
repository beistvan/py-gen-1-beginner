l, k = [input() for _ in range(int(input()))], int(input())
print(''.join([s[k - 1] for s in l if len(s) > k - 1]))
