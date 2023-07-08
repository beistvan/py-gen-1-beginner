from math import log;
n = int(input())
print(sum((1 / (i + 1)) for i in range(n)) - log(n))
