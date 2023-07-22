palindromes = [p for p in range(100, 1001) if str(p) == str(p)[::-1]] 

print(palindromes)
