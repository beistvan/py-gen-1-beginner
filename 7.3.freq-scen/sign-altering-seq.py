n = int(input())
print(sum( (-1)**(i + 1) * i for i in range(n + 1) ))
