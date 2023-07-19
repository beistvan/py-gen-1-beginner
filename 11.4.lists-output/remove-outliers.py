k = [int(input()) for _ in range(int(input()))]
k.remove(min(k))
k.remove(max(k))
print(*k, sep='\n')
