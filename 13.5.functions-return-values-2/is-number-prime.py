from sympy import isprime

def is_prime(num):
    return isprime(num)

n = int(input())

print(is_prime(n))
