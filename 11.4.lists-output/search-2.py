s = [input() for _ in range(int(input()))]
g = [input().lower() for _ in range(int(input()))]
for i in range(len(s)):
    c = 0
    for j in range(len(g)):
        if g[j] in s[i].lower():
            c += 1
    if c == len(g):
        print(s[i])
