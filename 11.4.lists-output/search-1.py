s = [input() for _ in range(int(input()))]
g = input().lower()
print(*[s[i] for i in range(len(s)) if g in s[i].lower()], sep="\n")
