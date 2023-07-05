n = int(input())
print("YES" if 999 < n < 10000 and (n % 7 == 0 or n % 17 == 0) else "NO")
