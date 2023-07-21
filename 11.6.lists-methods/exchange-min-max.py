s = [int(i) for i in input().split()]
ind_max, ind_min = s.index(max(s)), s.index(min(s))
s[ind_min], s[ind_max] = s[ind_max], s[ind_min]
print(*s)
